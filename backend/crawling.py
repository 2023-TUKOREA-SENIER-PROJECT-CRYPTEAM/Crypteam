# 필요한 라이브러리 import
import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pymysql
import sqlalchemy
from sqlalchemy import create_engine
class news_bot:
    def __init__(self, keyword) -> None:
        self.keyword = keyword
        self.default_url = "https://www.google.com/"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def run(self):
        self.driver.get(self.default_url)
        time.sleep(1)

        sender = self.driver.find_element(By.CSS_SELECTOR, "#APjFqb")
        sender.send_keys(str(self.keyword) + Keys.ENTER)
        news_btn = self.driver.find_element(By.CSS_SELECTOR, "#hdtb-msb > div:nth-child(1) > div > div:nth-child(3) > a")
        news_btn.click()

        data = []
        while True:
            try:
                line_data = self.driver.find_elements(By.CSS_SELECTOR, "#rso > div > div > div")

                for line in line_data:
                    title = line.find_element(By.CSS_SELECTOR, "div > div > a > div > div.iRPxbe > div.mCBkyc.ynAwRc.MBeuO.nDgy9d").text
                    href = line.find_element(By.CSS_SELECTOR, "div > div > a").get_attribute("href")
                    date = line.find_element(By.CSS_SELECTOR, "div > div > a > div > div.iRPxbe > div.OSrXXb.ZE0LJd.YsWzw > span").text
                    data.append([title, href, date, self.keyword])

                self.driver.find_element(By.CSS_SELECTOR, "#pnnext").click()
            except:
                self.driver.quit()
                break
        df = pd.DataFrame(data, columns=["제목", "링크", "시간", "코인 이름"])
        # df.to_csv(self.keyword + "_news_data.csv")
        return df
        
def connect_db():
    host = "127.0.0.1"
    port = 3306
    username = "root"
    database = "NewsData"
    password = "825582qaz"
    try:
        con = pymysql.connect(host=host, user=username, password=password,
                        db=database, charset='utf8') # 한글처리 (charset = 'utf8')
    except:
        print(">> Connection 실패")
        return False

    return con
def Creat_db_table(name):
    con = connect_db()
    cur = con.cursor()
    ck_name = name.replace(" ", "")
    sql = '''CREATE TABLE '''+ ck_name +'''(
            Coin_name VARCHAR(1024),
            Title VARCHAR(1024),
            Url VARCHAR(1024),
            Date VARCHAR(1024)
            )
    '''
    try:
        cur.execute(sql) # sql문  실행
    except:
        pass
    # try:
    #     cur.execute(sql) # sql문  실행
    #     print(">> "+ck_name+" 테이블 생성 성공!")
    # except pymysql.err.OperationalError:
    #     print(">> 테이블 생성 실패 : 이미 생성된 테이블입니다.")
    #     return False
    # except pymysql.err.ProgrammingError:
    #     print(">> 테이블 생성 실패 : sql문 에러입니다.")
    #     return False
    con.close()
    cur.close()

def Insert_db_table(df,name):
    host = "127.0.0.1"
    port = 3306
    username = "root"
    database = "NewsData"
    password = "825582qaz"
    name_dic = {
        "비트코인" : "bitcoin",
        "이더리움" : "ethereum",
        "카르다노 에이다" : "cardanoada",
        "리플" : "xrp",
        "이더리움 클래식" : "etherumclassic",
    }
    try:
        db_connection_str = "mysql+pymysql://"+username+":"+password+"@"+host+"/"+database
        db_connection = create_engine(db_connection_str)
        conn = db_connection.connect()
        
    except:
        print(">> Connection 실패")
        return df
    
    dtypesql = { 
            'news_title':sqlalchemy.types.VARCHAR(1024), 
            'news_url':sqlalchemy.types.VARCHAR(1024),
            'news_registered_date':sqlalchemy.types.VARCHAR(1024),
            'coin_name':sqlalchemy.types.VARCHAR(1024)
    }
    
    # try:
    name = "newsdata_" + name_dic[name]
    df.to_sql(name = name,con = conn,if_exists='append',index=False,dtype = dtypesql)
    conn.close()
        
    return True
    # except:
        
    #     print(">> 데이터 업로드 실패... 파라미터를 확인하세요")
    #     return df

searching_keyword = ["비트코인", "이더리움", "리플", "이더리움 클래식", "카르다노 에이다"]
temp = ["카르다노 에이다"]
for name in searching_keyword:
    # Creat_db_table(name)
    bot = news_bot(name)
    df = bot.run()
    df.columns = ["news_title", "news_url", "news_registered_date", "coin_name"]
    Insert_db_table(df, name)
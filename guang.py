def getFileName(filepath):
    """获得解析引文名列表"""
    filename = []
    for root,dirs,files in os.walk(filepath):
        for file in files:
            filename.append(root + os.sep + file)
    return filename

def insertsql(cur,sql,values):
    """
    执行sql操作
    """
    cur.execute(sql,values)
    return  None


if __name__=="__main__":
    conn=cx_Oracle.connect("NEWPATENT","NEWPATENT","192.168.0.213/orcl")
    cur=conn.cursor()
    path="K:\\tongzu"
    sql="""insert into NEWPATENT.patent_family(patent_family,patent_id,id)
           VALUES (:patent_family,:patent_id,:id)"""
    filenames=getFileName(path)
    patent_id=222066 + 1
    id=968283+1
    dicts={}
    for filename in filenames:
        print(filename)
        data=pd.read_excel(filename)
        data=data.fillna("miss")
        for i in range(data.shape[0]):
            if data['inpadoc同族'].values[i]!='miss':
                if 'CN' in data['inpadoc同族'].values[i]:
                    for onedata in data['inpadoc同族'].values[i].split(";"):
                        dicts['patent_family']=onedata
                        dicts['patent_id']=patent_id
                        dicts['id']=id
                        id+=1
                        insertsql(cur, sql, dicts)
                        print(dicts)
                    patent_id += 1



        conn.commit()
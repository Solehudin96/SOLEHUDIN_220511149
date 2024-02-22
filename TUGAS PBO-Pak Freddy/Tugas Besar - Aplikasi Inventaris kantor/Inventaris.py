from dblocallhost import DBConnection as mydb
class Inventaris:
    def __init__(self):
        self.__id=None
        self.__kode_barang=None
        self.__nama_barang=None
        self.__ruangan=None
        self.__kondisi_barang=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def kode_barang(self):
        return self.__kode_barang
        
    @kode_barang.setter
    def kode_barang(self, value):
        self.__kode_barang = value
    @property
    def nama_barang(self):
        return self.__nama_barang
        
    @nama_barang.setter
    def nama_barang(self, value):
        self.__nama_barang = value
    @property
    def ruangan(self):
        return self.__ruangan
        
    @ruangan.setter
    def ruangan(self, value):
        self.__ruangan = value
    @property
    def kondisi_barang(self):
        return self.__kondisi_barang
        
    @kondisi_barang.setter
    def kondisi_barang(self, value):
        self.__kondisi_barang = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_barang,self.__nama_barang,self.__ruangan,self.__kondisi_barang)
        sql="INSERT INTO Inventaris (kode_barang,nama_barang,ruangan,kondisi_barang) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_barang,self.__nama_barang,self.__ruangan,self.__kondisi_barang, id)
        sql="UPDATE inventaris SET kode_barang = %s,nama_barang = %s,ruangan = %s,kondisi_barang = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByKODE_BARANG(self, kode_barang):
        self.conn = mydb()
        val = (self.__nama_barang,self.__ruangan,self.__kondisi_barang, kode_barang)
        sql="UPDATE inventaris SET nama_barang = %s,ruangan = %s,kondisi_barang = %s WHERE kode_barang=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM inventaris WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByKODE_BARANG(self, kode_barang):
        self.conn = mydb()
        sql="DELETE FROM inventaris WHERE kode_barang='" + str(kode_barang) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM inventaris WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__kode_barang = self.result[1]
        self.__nama_barang = self.result[2]
        self.__ruangan = self.result[3]
        self.__kondisi_barang = self.result[4]
        self.conn.disconnect
        return self.result
    def getByKODE_BARANG(self, kode_barang):
        a=str(kode_barang)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM inventaris WHERE kode_barang='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__kode_barang = self.result[1]
           self.__nama_barang = self.result[2]
           self.__ruangan = self.result[3]
           self.__kondisi_barang = self.result[4]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__kode_barang = ''
           self.__nama_barang = ''
           self.__ruangan = ''
           self.__kondisi_barang = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM inventaris"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nama_barang FROM inventaris"
        self.result = self.conn.findAll(sql)
        return self.result    
# COMPLETE MONGODB & PY-MONOG CHEAT-SHEET
# https://www.mongodb.com/docs/v3.0/reference/

# --BASICS--

# TO VIEW ALL THE DATA-BASE
# show dbs

# TO VIEW ALL THE COLLECTIONS
# show collections

# TO DROP THE DATABASE 
# 1. use <db>
# 2. db.dropDatabase()

# TO DROP A COLLECTIONS
# 1. show collections
# 2.db.<collections-name>.drop()

# TO CREATE A COLLECTIONS 
# db.createCollecitons("name", [option] )
# Pass Query : db.<collection-name>.insertOne()

# TO RESTORE THE DELETED COLLECTION'S OR DB
# NOTE : STANDALONE'S WONT CREATE ANY REPLICA OF DATA :  NOTE
# https://www.mongodb.com/docs/ops-manager/current/tutorial/restore-single-database/

# --INTERMEDIATE--

        # INSERTING DOCUMENT'S : ALL CREATE OPERAIONS NOTE NOTE

# ONE : db.<collection-name>.insertOne({key:value})
# MANY : db.<collection-name>.insertMany([{key:value},{key:value}]) # ARRAY MUST BE USED 

        # FINDING DOCUMENT'S  : ALL READ OPERATIONS NOTE NOTE

# SPECIFIC_VALUE : db.<collection-name>.find({key:value})
# USING_OPERATOR : db.<collection-name>.find({key : {$eq : value}})
# FIND_ONE : db.<collection-name>.findOne()

# IN_OPERATOR : db.<collection-name>.find({key : {$in : [value,value]}})
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-insert-and-find-documents/lesson-2-finding-documents-in-a-mongodb-collection/learn?client=customer&page=2

        # COMPARISION OPERATOR'S

# > : db.<collection-name>.find({key : {$gt : value}})
# >= : db.<collection-name>.find({key : {$gte : value}})
# < : db.<collection-name>.find({key : {$lt : value}})
# <= : db.<collection-name>.find({key : {$lte : value}})

        # ARRAY QUERY OPERATION'S : Get all the documents who's elements matches given values

# db.<collection-name>.find({key : {$elemMatch : {key:value,key:value,key:value}}})
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-insert-and-find-documents/lesson-4-querying-on-array-elements-in-mongodb/learn?client=customer&page=2

        # LOGICAL OPERATOR'S

# AND : db.<collection-name>.find({key:value},{key:value}) *NOTE* db.<collection-name>.find($and : [{key:value},{key:value}])
# OR : db.<collection-name>.find($or :[{key:value},{key:value}])

        # REPLACE A DOCUMENT : ALL UPDATE OPERATION'S NOTE NOTE

# db.<collection-name>.replaceOne({_id : },{key : value})

# TO CHECK
# db.<collection-name>.findOne({_id})

        # UPDATE DOCUMENT 
# They have 3 methods: $set , $push , $upsert

# FOR SET NOTE
# $set -- ALREADY EXISTING VALUE YOU REPLACE 
# db.<collection-name>.updateOne({_id},{$set : {key:value}})

# FOR PUSH NOTE
# $push -- YOU PUSH A NEW VALUE TO A DOCUMENT 
# db.<collection-name>.updateOne({_id}, {$push : {key:value}})

# FOR UPSERT NOTE
# $upsert -- UPDATE & SET : CREATE'S ONE IF NOTHING EXIST'S
# db.<collection-name>.updateOne({_id}, {$set : {key : value}} , {upsert : true})

# FIND AND MODIFY DOCUMENT : UPDATE AND RETURN SAME DOCUMENT NOTE --------------------------- Need to check
# find() + update() : $updateAndModify()
# db.<collection-name>.findAndModify({query : {[selection] key : value}, update : {key:value}, new : true})

# UPDATEMANY NOTE THEY DO NOT HAVE ROLLBACK OPTION - UPDATE MULTIPLE DOCUMENT
# updateMany()
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-replace-and-delete-documents/lesson-4-updating-mongodb-documents-by-using-updatemany/learn?client=customer&page=2
# db.<collection-name>.updateMany({key:value},{$set : {key:value}}) # all key with that value will be updated

        # DELETEING DOCUMENT : ALL DELETE DOCUMENT NOTE NOTE
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-replace-and-delete-documents/lesson-5-deleting-documents-in-mongodb/learn?client=customer&page=2

# db.<collection-name>.find()
# db.<collection-name>.deleteOne({_id}) # deleteOne document
# db.<collection-name>.deleteMany({key:value}) # deleteMany document

        # SORT AND LIMIT : NOTE NOTE
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-modifying-query-results/lesson-1-sorting-and-limiting-query-results-in-mongodb/learn?client=customer&page=2
# <cursor-name>.sort() , <cursor-name>.limmit()

# NOTE : CAP letter will be grouped and sorted first and then LOW letters

# NOTE : You can use -1 to not include element too , you can also supress the field by using 0

#  SORT
# db.<collection-name>.find({key:value}).sort({key : 1}) # ascending order
# db.<collection-name>.find({music : "jazz"},{name : 1}).sort({name:-1}) # descending order

# LIMIT
# db.<collection-name>.find({key:value}).sort({key : 1}).limit(3)

        # PROJECTION : Returning selected field from all document NOTE

# IN PROJECTION WE CANNOT INCLUDE AND EXCLUDE IN THE SAME QUERY NOTE NOTE

# db.<collection-name>.find({name: <user-input>},{password : 1})
# db.<collection-name>.find({name: <user-input>},{password : 1,name:1,_id:0})

# https://learn.mongodb.com/learn/course/mongodb-crud-operations-modifying-query-results/lesson-2-returning-specific-data-from-a-query-in-mongodb/learn?client=customer&page=2

        # COUNTING DOCUMENTS : NOTE
# countDocuments({<query>})
# db.<collection-name>.countDocuments({key : {$gt : value}})

                # CRUD OPERATION USING PYTHON : NOTE NOTE NOTE NOTE NOTE

# They use BSON {binary Json} and extension of JSON : They are also represented in DICTIONARY FORMATE
# They are used to STORE and ORGANIZE , Easy for RETRIVAL
# Secure than json , and support MULTIPLE DATATYPE 
# obj_id type is represented as an instance of the objectId clas 

        # USING pymongo {PYTHON & MONGODB} NOTE NOTE NOTE 

# 1. Imporitn the library
# from pymongo import mongoClient

# 2. Initalize the connection
# conn = pymongo.mongoClient("<connection string from atlas")

# 3. Creating the DataBase
# db = conn['data-base]

# 4. Creating the Collection
# col = db.<collection-name>

# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE 































# PYMONGO ARROW NOTE NOTE
# NOTE NOTE NOTE NOTE NOTE NOTE DATA SCICNE RELATED NOTE NOTE NOTE NOTE 
# They are an extension of pymonog library, They are used to load PANDAS, NUMPY etc (and the OTHER WAY AROUND)
# They use APACHE ARROW 

# -> installation : 
# pip install pymongoarrow

 












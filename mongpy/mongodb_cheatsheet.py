# This is complete cheatsheet for pymongo and monogdb

# Whenever you have field names like "naruto.zip" always use the double quotation mark or else you will get the error

# NOTE : $in and $elemmatch - working

                        # Mongodb-Cheatsheet

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
# db.createCollecitons("name",[options])
# or just pass-query : db.<collection-name>.insertOne()

# TO RESTORE THE DELETED COLLECTIONS OR DATABASE
# https://www.mongodb.com/docs/ops-manager/current/tutorial/restore-single-database/
# BUT WITH STAND-ALONE IT WONT CREATE ANY REPLICA OF THE SET SO DATA IS DOOMED :(

# 1. Inserting a Document
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-insert-and-find-documents/lesson-2-finding-documents-in-a-mongodb-collection/learn?client=customer


        # db.<collection-name>.insertOne({"name":"hari","s_name":"prasad"})
        # db.<collection-name>.insertMany({"name":"hari"},{"s_name" :"prasad"})

# 2. Finding a Document

        # db.<collection-name>.find({})
        # db.<collection-name>.find({"a" : {$eq : 10}})
        # db.<collection-name>.findOne({})

# 3. This opertor is used when dealing with ARRAY

# If this ele is there IN this ARRAY : $in
# # https://learn.mongodb.com/learn/course/mongodb-crud-operations-insert-and-find-documents/lesson-2-finding-documents-in-a-mongodb-collection/learn?client=customer&page=2


        # db.<collection-name>.find({some-array-name : {$in : 'name'}})
        # db.<collection-name>.find({some-array-name : {$in : ['name','name]}})
 
# 4. Comparision Operator

        # $gt : db.<collection-name>.find({'salary':{$gt : 5000}}) : >
        # $lt : db.<collection-name>.find({'salary':{$lt : 5000}}) : <
        # $lte : db.<collection-name>.find({'salary':{$lte : 5000}}) : <=
        # $gte : db.<collection-name>.find({'salary':{$gte : 5000}}) : >=

# https://www.mongodb.com/docs/manual/reference/operator/query-comparison/
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-insert-and-find-documents/lesson-3-finding-documents-by-using-comparison-operators/learn?client=customer&page=2

# 5. Querying in an ARRAY : Finding any element is MATCHING INSIDE AN ARRAY --------- FOCUS MORE

        # db.<collection-name>.find({array-name:{$elemMatch : {$eq : 2000}}}) 
# # https://learn.mongodb.com/learn/course/mongodb-crud-operations-insert-and-find-documents/lesson-4-querying-on-array-elements-in-mongodb/learn?client=customer&page=2

# 6. Logical Operator 

        # $and : db.<collection-name>.find({"name":"a"},{"age":20})
        # $and : db.<collection-name>.find($and : [{"name":"hari"},{"age":20}])
        # $or : # $and : db.<collection-name>.find($or : [{"name" : "hari"}, {"name" : "hemanth"}])

# https://learn.mongodb.com/learn/course/mongodb-crud-operations-insert-and-find-documents/lesson-5-finding-documents-by-using-logical-operators/learn?client=customer&page=2
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-insert-and-find-documents/conclusion/first-lesson?client=customer&page=2

# 7. Replace Document
# Note : Make sure you mention other element while replacing 
        # db.<collection-name>.replaceOne({_id},{"some-ele" : "some-value"})

# TO CHECK IF IT'S REPLACED

        # db.<collection-name>.findOne({_id})

# 8. Update Document
# an Update has three methods  : $set , $push , $upsert

# db.<collection-name>.updateOne({_id},{"some-ele":"some-value"})

        # $set -- they add element / replace

# db.<collection-name>.updateOne({_id},{$set : {"some-ele":"some-value"}})

        # $push -- they work same as append 

# db.<collection-name>.updateOne({_id},{$push : {"some-ele":"some-value"}})

        # $upsert -- they work as UPDATE AND INSERT

        
        # db.<collection-name>.updateOne({"title" : "some-contenet"}, {$set : {"pop-corn": true}},upsert : true)

# https://learn.mongodb.com/learn/course/mongodb-crud-operations-replace-and-delete-documents/lesson-2-updating-mongodb-documents-by-using-updateone/learn?client=customer&page=2

# 9. findandModify()  :update and return the same document : find() + update() # WORKS FOR ONE 

        # db.<collection-name>.findAndModify({ query : {<selection}, update:{<changes>},new: true / false})
        # db.<collection-name>.findAndModify({ query : {<selection}, update:{$inc : {salary : 1}},new: true / false})

# 10. updateMany() : update many documents : when the option fails it dosent roll back the options

# <filter-document : selection ><update-document : the modificaiton >

# https://learn.mongodb.com/learn/course/mongodb-crud-operations-replace-and-delete-documents/lesson-4-updating-mongodb-documents-by-using-updatemany/learn?client=customer
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-replace-and-delete-documents/lesson-4-updating-mongodb-documents-by-using-updatemany/learn?client=customer&page=2

# db.<colleciton-name>.updateMany({common_name : {$in : ["a","b"]}},{$set : {last_seen : ("some-date")}})

# 11. deleteOne() and deleteMany() : Deleting the document 

# deleting the duplicate document 
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-replace-and-delete-documents/lesson-5-deleting-documents-in-mongodb/learn?client=customer&page=2

# db.<collection-name>.find()
# db.<collection-name>.deleteOne({_id})

# deleting the multiple document 

# db.<colleciton-name>.find({category : "crime"})
# db.<collection-name>.deleteMany({category : "crime"})

# https://learn.mongodb.com/learn/course/mongodb-crud-operations-replace-and-delete-documents/conclusion/learn?client=customer&page=2

# 12. Return in a format way
# cursor.sort() and cursor.limit()

# CURSOR : pointer to the result set of query
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-modifying-query-results/lesson-1-sorting-and-limiting-query-results-in-mongodb/learn?client=customer&page=2

# 1.for sort
# db.<collection-name>.find({category: "music"}).sort({name : 1}) # ascending order 
# db.<collection-name>.find({category: "music"},{name:1 # projection, number_of_years : {$gt : 2}}).sort({name : -1}) # descending order

# NOTE : CAP letters will be grouped and sorted first and then LOW letters

# NOTE : you can use -1 to not include element too

# NOTE : you can also supress the field by using 0

# 2. We use limit for unnecessary data processing :

# db.<collection-name>.find({category: "music"},{name:1 # projection}).sort({name : -1}) # here we only want the top 3 or 2
# db.<collection-name>.find({category: "music"},{name:1 # projection}).sort({name : -1}).limit(3)

# 3. Returning selected fields from the mongodb  : PROJECTION
# WE CANNOT INCLUDE AND EXCLUDE FIELD IN THE PROJECTION AT THE SAME TIME WE CAN SUPRESS THEM BUT NOT EXCLUDE

# like if you want only the user-name : Refered as Projection
# by using this we can create a login page

# Ex : db.login.find({name: <user-input>},{password : 1})

# if <user-input-password> == password --- grant access 
# [ { _id: ObjectId('65ac9e2ba69df9cb49ca8ca6'), password: 'xyz' } ]

# Ex to add multiple field : db.login.find({name: <user-input>},{password : 1,name:1,_id:0})

# https://learn.mongodb.com/learn/course/mongodb-crud-operations-modifying-query-results/lesson-2-returning-specific-data-from-a-query-in-mongodb/learn?client=customer&page=2

# 4. COUNTING DOCUMENTS : how to count the number of documents
# db.<collection-name>.countDocuments(<query>,<option : count behaviour>)
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-modifying-query-results/lesson-3-counting-documents-in-a-mongodb-collection/learn?client=customer&page=2
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-modifying-query-results/conclusion/learn?client=customer&page=2

# 5. CRUD OPERATIONS using python
# they use BSON {Binary JSON} an extension of JSON ; BSON also represented in a dictonary format
# they are used to organize and store the data and retrival 
# more secure than json and support more json datatype

# Using Pymongo ; they include bson package 
# dictionary are called : Sub-Document
# https://learn.mongodb.com/learn/course/mongodb-crud-operations-in-python/lesson-1-working-with-mongodb-documents-in-python/learn?client=customer

# PRACTICALS 

# USING PYTHON AND MONGODB
                                                        #{initating a connection}
# from pymongo import mongo_client
# conn = mongo_client()
# db = conn['db-name']
# col_cars= db.cars

# Add the <connection-string> form IDE to MongoDB-Atlas using terminal
# Init a data-base
# create a collection -> to insert document

# inserting the document in the python

# insert_one() single
# insert_many() multiple

# insert_one and insert_many
#https://learn.mongodb.com/learn/course/mongodb-crud-operations-in-python/lesson-2-inserting-a-document-in-python-applications/learn?client=customer&page=2


# Initiating a connection and creating a database and a connection and add a value and search a value using python

































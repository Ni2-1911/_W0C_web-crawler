#each website you crawl get seprate project
import os
def create_project_dir(directory):
    if not os.path.exists(directory):
        #print('Creating project: ' + directory)
        os.mkdir(directory)

def create_data_files(project_name,file_name):
    path = project_name + '/' + file_name
    f = open(path, 'w')
    f.close()
    print("file created: " + path)

#creating new file
def write_file(path,data):
    f = open(path, 'w')
    f.write(data)
    f.close()


#add data in 
def append_to_file(path , data):
    with open(path , 'a') as file:
        file.write(data + '\n')
 

#delete the contents in file content
def delete_file_content(path):
    with open(path ,'w'):
        pass

#read a file and convert each line to set items
def file_to_get(file_name):
    results = set()
    with open(file_name , 'rt') as f :
        for line in f:
            results.add(line.replace('\n' , ''))
        return results

#iterate through a set, each item will be a new line in a file
def set_to_file(links,file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file ,link)



#examples
#create_project_dir('nitu')
#create_data_files('google','depth0')
#write_file('nitu/depth0.txt','this is depth0 file')




















 

# set PATH=D:\Apps\Python35;%PATH%
import os
import glob
from os.path import basename, splitext

"""
import sys 
from os import listdir
from os.path import isfile, join, basename, splitext
"""

def get_name(file):
    return splitext(basename(file))[0]
    
def get_version(file):
    dot_index = file.find('.')
    if file[dot_index-1:].find('.') != -1 and file[dot_index-1:].find('/') != -1:
        slash_index = file[dot_index-1:].index('/')
        return file[dot_index-1 : dot_index-1 + slash_index]
    else:    
        return '0.9'

def list_jars(path, recursiv=False):        
    names = set()
    files = glob.glob(path, recursive=recursiv)
    for file in files:    
        name = str(file)
        name = name.replace('\\', '/')
        names.add(name)        
    return names

def write_mvn_install(files, out):    
    with open(out, "w") as out_file:
        for file in files:
            print("mvn install:install-file -Dfile={0} -DgroupId=com.example.tcs -DartifactId={1} -Dversion={2} -Dpackaging=jar".format(file, get_name(file), get_version(file)), file=out_file)


def write_mvn_dependencies(files, out):
    with open(out, "w") as out_file:
        for file in files:
            print("<dependency>", file=out_file)
            print("    <groupId>com.example.tcs</groupId>", file=out_file)
            print("    <artifactId>{0}</artifactId>".format(get_name(file)), file=out_file)
            print("    <version>{0}</version>".format(get_version(file)), file=out_file)
            print("</dependency>", file=out_file)

def main_tc():
    base = 'D:/home/tc/web/lib/jars/tcs/'
    flat = base + '*.jar'
    nested = base + '**/*.jar' 
        
    flat_jars = list_jars(flat, recursiv=False) # 19 matching jars
    nested_jars = list_jars(nested, recursiv=True) - flat_jars # 85 - 19 = 66 matching nested jars
    
    flat_jars = sorted(flat_jars)
    nested_jars = sorted(nested_jars)
    
    print('\n'.join(flat_jars))    
    print('\n')
    print('\n'.join(nested_jars))

    out = 'D:/home/sa/web/tmp/'
    write_mvn_install(flat_jars, out + '01_tc_mvn_install.sh')
    write_mvn_dependencies(flat_jars, out + '01_tc_mvn_pom.xml')
    write_mvn_install(nested_jars, out + '02_tc_mvn_install.sh')
    write_mvn_dependencies(nested_jars, out + '02_tc_mvn_pom.xml')
    
    
def main_shared():
    base = 'D:/home/tc/shared/build/libs/'
    flat = base + '*.jar'
    
    flat_jars = sorted(list_jars(flat, recursiv=False))
    print('\n'.join(flat_jars))    
    
    out = 'D:/home/sa/web/tmp/'
    write_mvn_install(flat_jars, out + '03_shared_mvn_install.sh')
    write_mvn_dependencies(flat_jars, out + '03_shared_mvn_pom.xml')
    
    
def main_tc2():
    files = """D:/home/tc/web/lib/jakarta-struts-1.1/lib/struts.jar
D:/home/tc/web/lib/jars/TestServices.jar
D:/home/tc/web/lib/jars/activation.jar
D:/home/tc/web/lib/jars/asyncservices.jar
D:/home/tc/web/lib/jars/axis_dok.jar
D:/home/tc/web/lib/jars/bfograph.jar
D:/home/tc/web/lib/jars/docusign/eSignJavaLib.jar
D:/home/tc/web/lib/jars/fileconvert.jar
D:/home/tc/web/lib/jars/httpunit.jar
D:/home/tc/web/lib/jars/ifxjdbc.jar
D:/home/tc/web/lib/jars/imgscalr-lib-4.2.jar
D:/home/tc/web/lib/jars/itext-1.1.jar
D:/home/tc/web/lib/jars/jdom-1.1.3.jar
D:/home/tc/web/lib/jars/jive/htmlparser.jar
D:/home/tc/web/lib/jars/jive/jivebase.jar
D:/home/tc/web/lib/jars/jive/jiveforums.jar
D:/home/tc/web/lib/jars/jive/velocity-dep.jar
D:/home/tc/web/lib/jars/ldap.jar
D:/home/tc/web/lib/jars/netscape_ldap_sdk.jar
D:/home/tc/web/lib/jars/rome-1.0.jar
D:/home/tc/web/lib/jars/spring.jar
D:/home/tc/web/lib/jars/tc.jar"""

    files = """D:/home/tc/web/lib/jars/jboss/scheduler-plugin.jar"""
                
    flat_jars = sorted(files.split('\n'))
    print('\n'.join(flat_jars)) 
    
    out = 'D:/home/sa/web/tmp/'
    write_mvn_install(flat_jars, out + '04_tc_mvn_install.sh')
    write_mvn_dependencies(flat_jars, out + '04_tc_mvn_pom.xml')

if __name__ == "__main__":
    #main_tc()
    #main_shared()
    main_tc2()
    
    
    


#Lista las tareas pendientes para un sitio web a traves de taskwarrior
#USO:
#En el directorio del proyecto
#Escribir: taskgen
#Listo

import csv
import os
import commands
cwd = os.getcwd()
cwd = cwd.split("/")
cwd = cwd[-1]
tags = ""
with open('Tasks.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
                joined = ' '.join(row)
                joined = joined.split('"')
                taskDescription = joined[0]
                taskTags = joined[1]
                taskTags = taskTags.split()
                for tag in taskTags:
                        tags += " +"+tag


                line = "task add "+taskDescription+" project:"+cwd+" "+tags
                line = line.replace(",", "")
                print line
                commands.getoutput(line)
                tags = ""       

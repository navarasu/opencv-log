from shutil import rmtree
import os
import cvlog.html_template as ht
import datetime
import json
from inspect import stack
from datetime import datetime,timezone
from uuid import uuid4
class HtmlLogger:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__last_pos=-len(ht.CONTENT_END)
        self.__create_file()
        self.__no_data=True
    
    def log_image(self,level,img_data):
        data=''.join(['<img src="data:image/png;base64, ',img_data,'"/>'])
        self.__append_log_item(level,data)

    def __append_log_item(self,level,log_detail):
        template='<div class="log-item" id="'
        template+=self.__unique_id()+'" onclick="show_data(this.id)"'
        short_stack,data=self.__get_log_info()
        data['level']=level
        template+="data='"+json.dumps(data)+"' logdata = '"+log_detail+"'>"
        template+='<h3 class="time">'+data['time_stamp']
        template+='<span class="level '+level.lower()+'">'+data['level']+'</span></h3>'
        template+='<p class="time">'+short_stack+'</p></div>'
        self.__append([template])
    
    def __append(self,html_text_seq):
        with open(self.__file_path, "rb+") as html:
            if(self.__no_data):
                html.seek(-len(ht.NO_DATA_CONTENT)+self.__last_pos,2)
                self.__no_data=False
            else:
                html.seek(self.__last_pos,2)
            html.write((''.join(html_text_seq).join(['\n',ht.CONTENT_END])).encode('utf-8'))
            html.truncate()

    def __create_file(self):
        dir_path=os.path.dirname(self.__file_path)
        if os.path.exists(dir_path):
            rmtree(dir_path)
        os.makedirs(dir_path)
        with open(self.__file_path, 'w') as html:
            html.writelines(['<html>',ht.STYLE,ht.SCRIPT,ht.CONTENT_START,ht.NO_DATA_CONTENT,ht.CONTENT_END])
    
    def __get_log_info(self):
        short_stack,long_stack= self.__stack_trace(6)
        return short_stack, {'time_stamp': datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(' '),
                'long_stack':long_stack}
    
    def __stack_trace(self,start_stack):
        stacks =stack()[start_stack:]
        stack_trace=""
        for x in stacks[:10]:
            stack_trace+=x.filename+":"+str(x.lineno)+"\n"
        return stacks[0].filename+":"+str(stacks[0].lineno),stack_trace
    
    def __unique_id(self):
        return str(uuid4())
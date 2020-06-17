import os
import cvlog.html_template as ht
import datetime
import json
import re
import time
from inspect import stack
from datetime import datetime, timezone # noqa
from uuid import uuid4
from cvlog.config import Config

class HtmlLogger:
    def __init__(self):
        self.__last_pos = -len(ht.CONTENT_END)
        self.__no_data = False
        self.__rotate_log()

    def log_image(self, level, log_type, img_data, msg):
        data = ''.join(['<img src="data:image/png;base64, ', img_data, '"/>'])
        self.__append_log_item(level, log_type, data, msg)

    def __append_log_item(self, level, log_type, log_detail, msg):
        template = '<div class="log-item" id="'
        template += self.__unique_id() + '" onclick="show_data(this.id)"'
        short_stack, data = self.__get_log_info()
        data['level'] = level
        data['log_type'] = log_type
        data['msg'] = msg
        template += "data='" + json.dumps(data) + "' logdata = '" + log_detail + "'>"
        template += '<div class="log-type">' + log_type + '</div>'
        template += '<h3 class="tvme">' + data['time_stamp']
        template += '<span class="level ' + level.lower() + '">' + data['level'] + '</span></h3>'
        if msg is not None:
            template += '<p class="description">' + msg + '</p>'
        template += '<p class="line">' + re.sub(r'^/', '', short_stack) + '</p></div>'
        self.__try_append([template])

    def __append(self, html_text_seq):
        self.__create_file()
        with open(self.__file_path(), "rb+") as html:
            if self.__no_data:
                html.seek(-len(ht.NO_DATA_CONTENT) + self.__last_pos, 2)
                self.__no_data = False
            else:
                html.seek(self.__last_pos, 2)
            html.write((''.join(html_text_seq).join(['\n', ht.CONTENT_END])).encode('utf-8'))
            html.truncate()

    def __try_append(self, html_text_seq):
        count = 0
        while self.__is_appended(html_text_seq) and count < 5:
            time.sleep(0.1)
            count += 1

    def __is_appended(self, html_text_seq):
        failed = False
        try:
            self.__append(html_text_seq)
        except IOError:
            failed = True
        return failed

    def __create_file(self):
        if os.path.exists(self.__file_path()):
            return
        dir_path = os.path.dirname(self.__file_path())
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(self.__file_path(), 'w') as html:
            html.writelines(['<html>', ht.STYLE, ht.SCRIPT, ht.CONTENT_START, ht.NO_DATA_CONTENT, ht.CONTENT_END])
        self.__no_data = True

    def __rotate_log(self):
        if Config().rotate_log() and os.path.exists(self.__file_path()):
            os.rename(self.__file_path(), self.__rename_file_path())

    def __rename_file_path(self):
        time_stamp = datetime.fromtimestamp(os.path.getctime(self.__file_path())).strftime("%y-%m-%d.%H%M%S")
        rename_path = os.path.join(Config().log_path(), 'cvlog_' + str(time_stamp) + '.html')
        if os.path.exists(rename_path):
            rename_path = os.path.join(Config().log_path(), 'cvlog_' + str(time_stamp) + '_01.html')
        if os.path.exists(rename_path):
            os.remove(rename_path)
        return rename_path

    def __get_log_info(self):
        short_stack, long_stack = self.__stack_trace(6)
        return short_stack, {'time_stamp': datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(' '),
                             'long_stack': long_stack}

    def __stack_trace(self, start_stack):
        stacks = stack()[start_stack:]
        stack_trace = ""
        for x in stacks[:10]:
            stack_trace += x.filename + ":" + str(x.lineno) + "\n"
        return stacks[0].filename + ":" + str(stacks[0].lineno), stack_trace

    def __unique_id(self):
        return str(uuid4())

    def __file_path(self):
        return os.path.join(Config().log_path(), "cvlog.html")

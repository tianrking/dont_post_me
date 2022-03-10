from shutil import register_archive_format
from markupsafe import escape
from flask import request
from flask import Flask, render_template, request
from flask import send_from_directory
import fnmatch

app = Flask(__name__)

import sys
import os
import you_get

def download(url, video_path,video_name):
    # sys.argv = ['you-get','-o', path, url]
    sys.argv = ['you-get','-o',video_path, '-O',video_name, url]
    you_get.main()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/test/get/<name>")
def hello(name):
    # return f"Hello, {escape(name)}!"
    return name

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # print("A")
        url = request.args.get("url")
        
        # ffmpeg -i input.flv output.mp4
        print(url)
        return request.method
    else:
        # return request.method
        username = request.form.get('username')
        url = request.form.get('url')
        print(type(url))
        
        # print("B\n")
        print(username)
        
        # url = 'https://www.bilibili.com/video/BV1HB4y1P7Ty'
        
        v_name = url.split("video/")[1]
        print(v_name)
        
        
            # download(url, "./media",v_name)
        os.system("rm -rf %s/%s*"%("./media",v_name))
        os.system("you-get -o %s -O %s %s"%("./media",v_name,url))
      
           
        try: 
            # print("Oh MY GOD")
            for GG in os.listdir('./media'):
                # search = ['*.mp4', '*.flv', '*.avi']
                # for KK in search:
                #     if fnmatch.fnmatch(GG, KK):
                #         # print(v_name+KK[2:])
                #         return send_from_directory('./media',v_name + KK[1:])
                print("Oh MY GOD")
                if fnmatch.fnmatch(GG, '%s*'%(v_name)):
                
                    print("OOOOOOOOOOOOOOO")
                    if fnmatch.fnmatch(GG, '*.flv'):
                        os.system('ffmpeg -i %s %s.mp4'%(GG,v_name), 'r')
                        return send_from_directory('./media',v_name+".mp4")
                        # print(output.read())
                    
                    if fnmatch.fnmatch(GG, '*.mp4'):
                        print("mp4")
                        return send_from_directory('./media',v_name+".mp4")
                
                return "ERROR"
            # GG = "media.mp4"
            # print(v_name)
            # return send_from_directory('./media',v_name)
            # return "T_T"    
            # return send_from_directory('./media','gg.flv')
        except Exception as e:
            return str(e)
        # return 'name = {}'.format(username)

# @app.route("/download/<d_name>")
# def _download(d_name):
#     # print(d_name)
#     return d_name

   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8111)
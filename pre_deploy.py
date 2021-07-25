#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys,os,time

sp = ['_navbar.md','_sidebar.md','README.md']

def write_readme(parent_path, dir_list, file_list, save_path):
    old_file = os.path.join(save_path,'README.md')
    if os.path.isfile(old_file):
        pass
        #os.remove(old_file)
    
    with open(old_file, 'w') as f:
        if parent_path == '.':
            tag_num = 1
        else:
            tag_num = len(parent_path.split('/'))+1
        
        for h_title in dir_list:
            h_path = os.path.join(parent_path, h_title, 'README.md')
            one = '{} [{}]({})\n'.format('#'*tag_num, h_title, h_path)
            f.write(one)
        for f_title in file_list:
            file_name = os.path.splitext(f_title)[0]
            file_path = os.path.join(parent_path, f_title)
            one = '- [{}]({})\n'.format(file_name, file_path)
            f.write(one)


def write_sidebar(parent_path, dir_list, file_list, save_path):
    sidebar_file = os.path.join(save_path,'_sidebar.md')
    
    with open(sidebar_file, 'w') as f:
        if parent_path != '.':
            back_name = '👈🏻 Go back'
            back_path = os.path.join(os.path.dirname(parent_path), 'README.md')
            go_back = '- [{}]({})\n'.format(back_name, back_path)
            f.write(go_back)

        for h_title in dir_list:
            h_path = os.path.join(parent_path, h_title, 'README.md')
            one = '- [{}]({})\n'.format(h_title, h_path)
            f.write(one)
        for f_title in file_list:
            file_name = os.path.splitext(f_title)[0]
            file_path = os.path.join(parent_path, f_title)
            one = '- [{}]({})\n'.format(file_name, file_path)
            f.write(one)


def main():
    app_path = os.getcwd()
    target_path = os.path.join(app_path, 'post/')
    for path,dir_list,file_list in os.walk(target_path):
        parent_path = os.path.relpath(path,start=target_path)
        file_list = [i for i in file_list if i not in sp]
        write_readme(parent_path, dir_list, file_list, path)
        write_sidebar(parent_path, dir_list, file_list, path)
        #print(parent_path, dir_list, file_list)

if __name__ == '__main__':
    main()
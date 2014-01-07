#!/usr/bin/env python
"""
Move a provided file to the trash on Mac OS X

Note: Only tested on OS X 10.9 (Mavericks)
"""
import os
import subprocess

def move_to_trash(file_path):
    """
    Move the provided file to it's closest Trash folder
    """
    # Get current user name
    user = os.path.expanduser('~').split('/')[-1]
    # Get current user id
    uid = os.geteuid()
    finder_pid = uid
    disk = file_path.split('/')[1]
    local_trash = os.path.join(os.path.expanduser('~'), '.Trash')
    if disk == 'Users':
        if os.path.exists(local_trash):
            print os.path.exists(file_path), os.path.exists(local_trash)
            subprocess.call('mv "{}" "{}"'.format(file_path, local_trash), shell=True)
        else:
            print 'ERROR: Can not find Trash'
    elif disk == 'Volumes':
        dirs = file_path.split('/')
        volume_trash = os.path.join(dirs[1], dirs[2], '.Trashes')
        if os.path.exists(volume_trash):
            users_volume_trash = os.path.join(volume_trash, str(uid))
            if os.path.exists(users_volume_trash):
                subprocess.call('mv "{}" "{}"'.format(file_path, users_volume_trash), shell=True)
            else:
                os.mkdir(users_volume_trash)
                subprocess.call('mv "{}" "{}"'.format(file_path, users_volume_trash), shell=True)
        elif os.path.exists(local_trash):
            subprocess.call('mv "{}" "{}"'.format(file_path, local_trash), shell=True)
        else:
            print 'ERROR: Can not find Trash'
        subprocess.call('mv "{}" "{}"'.format(file_path, local_trash), shell=True)
    else:
        print 'No idea whats happening...'

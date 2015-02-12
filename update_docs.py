#
# Script to collect all script documentations and add to gh-pages branch
# Only run on a UNIX based computer
#

import os

import settings


twitter_related_scripts = settings.INSTALLED_TWITTER_RELATED_SCRIPTS

template = (
    '---\n'
    'layout: post\n'
    'title: %(title)s\n'
    'source: %(source)s\n'
    '---\n'
    '%(content)s'
)

source = 'https://github.com/Soben713/Twizhoosh/tree/master/scripts/twitter_related/%s'


def delete_folder_contents(folder_path):
    os.system('rm -rf _posts')
    os.system('mkdir _posts')


def collect_docs():
    destination_folder_path = os.path.join(os.path.curdir, '_posts')
    delete_folder_contents(os.path.abspath(destination_folder_path))
    cnt = 2100

    for script_str in twitter_related_scripts:
        path = os.path.join(os.path.curdir, 'scripts', 'twitter_related', script_str, 'README.md')
        print("Exploring script %s" % script_str)

        if os.path.isfile(path):
            print("\tFound script documentation")

            readme_file = open(path)
            first_line = readme_file.readline()
            if '<!--ignore-->' in first_line:
                print("\tIgnored documentation")
                continue

            cnt -= 1
            script_name = first_line[2:].replace('\n', '')
            content = readme_file.read()

            destination_file_path = os.path.join(destination_folder_path, str(cnt) + '-01-01-' + script_str + '.md')
            destination_file = open(destination_file_path, 'w+')

            destination_file.write(template % {
                'title': script_name,
                'source': source % script_str,
                'content': content
            })

            destination_file.close()
            readme_file.close()


def exec_command(command):
    print('>' + command)
    ret = os.system(command)
    print(ret)
    return ret


if __name__ == "__main__":
    collect_docs()
    commands = """
    cp -rf _posts ..
    git checkout gh-pages
    git pull origin gh-pages
    rm -rf _posts
    mv ../_posts .
    git add --all
    git commit -m "Update _posts"
    git push origin gh-pages
    git checkout master
    """

    for command in commands.split('\n'):
        ret = exec_command(command)
        if not ret == 0:
            exec_command('git checkout master')
            break
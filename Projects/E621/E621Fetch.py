import urllib2, re, json, easygui, random, tempfile, subprocess, os;


# > Variables
posts = [];

# > URLS
e621_nav_url = 'https://e621.net/post/index/%d/';
e621_optimist = [
    'Furrys are awesome'
]

# > SCRIPT
def OptimistSays():
    return e621_optimist[random.randrange(len(e621_optimist))];

def SearchFurry(page, *searchTags):
    url = None;
    urlFile = None;
    matches = None;
    contentList = [];

    url = e621_nav_url % page;
    for tag in searchTags:
        url += tag + '%20';
    print url;

    urlFile = urllib2.urlopen(url);

    posts = re.findall('Post.register\(\{.*\}\);', urlFile.read());
    for post in posts:
        blockEx = None;
        blockPost  = None;

        blockEx = re.compile(r'{.*}');
        blockPost = blockEx.search(post);
        contentList.append(json.loads(blockPost.group(0)));

    return contentList;


if __name__ == '__main__':
    posts = None;
    postTags = [];
    postIndex = None;
    postImage = None;
    imageURL = None;
    choice = None;
    ynchoice = None;
    tempFile = None;

    search = True;
    running = True;
    
    while running:
        if search:
            searchKeywords = None;
            
            searchKeywords = easygui.enterbox('Search Tags:', 'E621: <' + OptimistSays() + '>');
            if searchKeywords:
                searchList = re.findall('[\w]+', searchKeywords);
                posts = SearchFurry(1, *searchList);
                search = False;
            else:
                break;

        postTags.append('> Search New Furries <');
        for post in posts:
            postTags.append(post['tags'].encode('utf8'));
        
        choice = easygui.choicebox('E621 Posts Found:', 'E621: <' + OptimistSays() + '>', sorted(postTags));

        try:
           if choice == '> Search New Furries <':
             search = True;
             continue

           if choice == None:
              running = False;

           if choice in postTags:
              postIndex = postTags.index(choice);
              imageURL = posts[postIndex-1]['file_url'];
              postImage = urllib2.urlopen(imageURL);
              tempFile = tempfile.NamedTemporaryFile(prefix='e621');

           with open(tempFile.name + '.png', 'wb') as imgFile:
               imgFile.write(postImage.read());

           subprocess.call(tempFile.name + '.png', shell = True);

           ynchoice = easygui.ynbox('Save the Image?', 'Image Worth');

           if ynchoice:
               imgFileName = None;
                    
               if not os.path.exists('Images'):
                   os.mkdir('Images');

               imgFileName = easygui.enterbox('Enter a filename:', 'Saving Image');

               imgFileName += '.png';
                        
               with open('Images/' + imgFileName, 'wb') as trueImgFile:
                    trueImgFile.write(postImage.read());

           os.remove(tempFile.name);
        except Exception as ex:
           print ex;
           input('Press enter key to continue...');

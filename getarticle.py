from bs4 import BeautifulSoup
import requests
import re
import codecs
import os

#links needed
login_url = 'http://www.homeschoolerpost.com/admin/'



def main():

    # file open and write
    f = codecs.open('compiledxml.txt', 'w+', encoding='utf-8')
    # headers
    f.write("Section\tPublish Date\tHide Data\tTitle\tContent\tMain Image Align\tMain Image\tMain Image Caption\tDetailed Image Align\tDetail Image\tDetailed Image Caption\tAuthor\tInclude In HomePage\tInclude In Featured Stories\tInclude In Top Stories\tInclude in News Ticker\tAllow Visitor Comments\tAllow Bookmark and Sharing\tScheduling Activated On\tScheduling Closed On\tMeta-Tag Keywords\tStatus")
    f.write(os.linesep)

    with requests.session() as s:

        payload = {
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        'ctl00$ContentPlaceHolder1$UserName':'hsc',
        'ctl00$ContentPlaceHolder1$Password':'johnholt',
        'ctl00$ContentPlaceHolder1$LoginButton':'Login',
        }

        # logging in
        login_page = s.get(login_url).content
        login_soup = BeautifulSoup(login_page, 'lxml')
        #payload["__VIEWSTATE"] = login_soup.select_one("#__VIEWSTATE")["value"]
        #payload["__VIEWSTATEGENERATOR"] = login_soup.select_one("#__VIEWSTATEGENERATOR")["value"]
        #payload["__PREVIOUSPAGE"] = login_soup.select_one("#__PREVIOUSPAGE")["value"]
        s.post(login_url, data=payload)

        edit_article_list = ["http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=299484","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=295611","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=296470","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=289719","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=280076","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=290224","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=290223","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=290226","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=290225","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=290222","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=290217","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=289685","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=289686","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=254360","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=276947","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=270195","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=243534","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=232633","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=221472","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=221207","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=221064","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=216163","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=216181","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=210357","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=202195","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=195229","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=185354","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=183958","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=183502","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=183501","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=175250","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=175246","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=148112","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=169185","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=167762","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=162577","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=144850","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=152073","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=153653","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=146838","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115428","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=148205","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=146847","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=146844","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=146843","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=146833","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=146831","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=146780","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=143317","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130067","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=116068","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=144790","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=143320","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=142210","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=142156","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=140891","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=140252","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=140391","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=138914","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=137904","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=137544","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=137003","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130144","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130218","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=136659","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=135500","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=131148","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115427","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130141","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130209","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130211","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130216","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130275","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130272","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130287","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130210","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130219","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130208","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130273","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130161","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130138","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130277","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130139","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130145","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130068","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130070","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130071","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130074","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130066","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=129871","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=129916","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=129874","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=129877","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=129876","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=129847","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=129917","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=129820","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=129819","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=119820","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=119816","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=119213","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=119200","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=119209","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=119199","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=119218","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=119212","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=118935","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=118692","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=118681","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115445","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130214","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=117599","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115446","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=117268","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=117267","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=114709","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=116061","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=116063","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=116030","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=116029","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=116028","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115952","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115727","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115829","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115801","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115823","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115450","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115448","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115447","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115423","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115796","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=114705","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115449","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115834","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=130215","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115995","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115993","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115842","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115839","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=114697","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115838","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=115724","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=114703","http://www.homeschoolerpost.com/Admin/AddEditArticle.aspx?ArticleID=114699"]


        for article_url in edit_article_list:
            article_edit_page = s.get(article_url, data=payload).text
            article_edit_soup = BeautifulSoup(article_edit_page, 'lxml')

            # Section
            if article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvArticle$ddlSubMenu"}) == None:
                continue
            else:
                for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvArticle$ddlSubMenu"}).findAll("option", {"selected":"selected"}):
                    f.write(thing.get_text(strip=True) + "\t")

            # Publish Date
            for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtPublishDate"})['value']:
                f.write(thing)
            f.write("\t")

            # Hide Data
            for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvArticle$DropDownList1"}).findAll("option", {"selected":"selected"}):
                f.write(thing.get_text(strip=True) + "\t")

            # Title
            for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtTitle"})['value']:
                thing1 = [re.sub(('\t'), ' ', e) for e in thing]
                for things in thing1:
                    f.write(things)
            f.write("\t")

            # Body/Content
            for thing in article_edit_soup.findAll("textarea", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtArticleContent"}):
                thing1 = [re.sub('(\n)', '<br>', e) for e in thing.contents]
                thing2 = [re.sub('(\r|\t)', ' ', e) for e in thing1]
                thing3 = [re.sub('<br>', '', e) for e in thing2]
                for things in thing3:
                    if 'img src=' in things:
                        athing = things[:things.find(".jpg") + len(".jpg")]
                    f.write(things)
            f.write("\t")

            # Main Image Align
            for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvArticle$ddlMainImageAlignment"}).findAll("option", {"selected":"selected"}):
                f.write(thing.get_text(strip=True) + "\t")

            # Main Image
            if article_edit_soup.findAll("a", {"id":"ctl00_ContentPlaceHolder1_fvArticle_lnkViewDetailedImage"}) != None:
                for thing in article_edit_soup.findAll("a", {"id":"ctl00_ContentPlaceHolder1_fvArticle_lnkViewMainImage"}):
                    f.write(thing.get('onclick').replace("MyPopup('../Files/", "").replace("');return false;", ""))
            f.write("\t")

            # Main Img Caption
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtMainImageCaption"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtMainImageCaption"})['value']:
                    thing1 = [re.sub(('\t'), ' ', e) for e in thing]
                    for things in thing1:
                        f.write(things)
            f.write("\t")

            # Detail Image Align
            for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvArticle$ddlDetailedImageAlignment"}).findAll("option", {"selected":"selected"}):
                f.write(thing.get_text(strip=True) + "\t")

            # Detailed Image
            if article_edit_soup.findAll("a", {"id":"ctl00_ContentPlaceHolder1_fvArticle_lnkViewDetailedImage"}) != None:
                for thing in article_edit_soup.findAll("a", {"id":"ctl00_ContentPlaceHolder1_fvArticle_lnkViewDetailedImage"}):
                    f.write(thing.get('onclick').replace("MyPopup('../Files/", "").replace("');return false;", ""))
            f.write("\t")

            # Detail Image Caption
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtDetailedImageCaption"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtDetailedImageCaption"})['value']:
                    thing1 = [re.sub(('\t'), ' ', e) for e in thing]
                    for things in thing1:
                        f.write(things)
            f.write("\t")

            # Author
            for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvArticle$ddlByLine"}).findAll("option", {"selected":"selected"}):
                f.write(thing.get_text(strip=True) + "\t")

            # Include In Home Page
            for thing in article_edit_soup.find_all("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$chkIncludedInHomePage", "checked":"checked"}):
                f.write("YES")
            f.write("\t")

            # Include In Featured Stories
            for thing in article_edit_soup.find_all("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$chkIncludedInFeatured", "checked":"checked"}):
                f.write("YES")
            f.write("\t")

            # Include In Top Stories
            for thing in article_edit_soup.find_all("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$chkIncludedInTopStories", "checked":"checked"}):
                f.write("YES")
            f.write("\t")

            # Include In New Ticker
            for thing in article_edit_soup.find_all("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$chkIncludedInNewsTicker", "checked":"checked"}):
                f.write("YES")
            f.write("\t")

            # Allow Visitor Comment
            for thing in article_edit_soup.find_all("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$chkCommentAllowed", "checked":"checked"}):
                f.write("YES")
            f.write("\t")

            # Allow Bookmark And Share
            for thing in article_edit_soup.find_all("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$chkBookmarkPlugin", "checked":"checked"}):
                f.write("YES")
            f.write("\t")

            # Scheduling Activate On
            for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtActivationDate"})['value']:
                f.write(thing)
            f.write("\t")

            # Scheduling Close On
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtClosingDate"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtClosingDate"})['value']:
                    f.write(thing)
            f.write("\t")

            # Meta-Key Word
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtMetaTagKeywords"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$txtMetaTagKeywords"})['value']:
                    thing1 = [re.sub(('\t'), ' ', e) for e in thing]
                    for things in thing1:
                        f.write(things)
            f.write("\t")

            # Status
            for thing in article_edit_soup.find_all("input", {"name":"ctl00$ContentPlaceHolder1$fvArticle$chkStatus", "checked":"checked"}):
                f.write("YES")
            f.write(os.linesep)



if __name__ == '__main__':
    main()
#javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvArticle','Page$3')

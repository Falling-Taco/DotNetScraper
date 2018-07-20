from bs4 import BeautifulSoup
import requests
import re
import codecs
import os

#links needed
login_url = ''



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
        'ctl00$ContentPlaceHolder1$UserName':'',
        'ctl00$ContentPlaceHolder1$Password':'',
        'ctl00$ContentPlaceHolder1$LoginButton':'Login',
        }

        # logging in
        login_page = s.get(login_url).content
        login_soup = BeautifulSoup(login_page, 'lxml')
        #payload["__VIEWSTATE"] = login_soup.select_one("#__VIEWSTATE")["value"]
        #payload["__VIEWSTATEGENERATOR"] = login_soup.select_one("#__VIEWSTATEGENERATOR")["value"]
        #payload["__PREVIOUSPAGE"] = login_soup.select_one("#__PREVIOUSPAGE")["value"]
        s.post(login_url, data=payload)

        edit_article_list = []

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

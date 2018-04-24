from bs4 import BeautifulSoup
import requests
import re
import codecs
import os

#links needed
login_url = 'http://valleycenterhappenings.com/admin/'



def main():

    # file open and write
    f = codecs.open('gotclassified.txt', 'w+', encoding='utf-8')
    # headers
    f.write("Section\tCategory\tTitle\tContent\tImage\tFeautured Priority\tScheduling\tFlag\tStatus")
    f.write(os.linesep)

    with requests.session() as s:

        payload = {
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        'ctl00$ContentPlaceHolder1$UserName':'admin',
        'ctl00$ContentPlaceHolder1$Password':'Happenings2017!',
        'ctl00$ContentPlaceHolder1$LoginButton':'Login',
        }

        # logging in
        login_page = s.get(login_url).content
        login_soup = BeautifulSoup(login_page, 'lxml')
        payload["__VIEWSTATE"] = login_soup.select_one("#__VIEWSTATE")["value"]
        payload["__VIEWSTATEGENERATOR"] = login_soup.select_one("#__VIEWSTATEGENERATOR")["value"]
        payload["__PREVIOUSPAGE"] = login_soup.select_one("#__PREVIOUSPAGE")["value"]
        s.post(login_url, data=payload)


        # Need to fix Image Part of this Script
        edit_article_list = ["http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10293","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11979","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11977","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11975","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11973","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11972","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11974","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11950","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11956","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11949","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11878","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11948","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11945","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11867","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11863","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11862","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11859","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11852","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11853","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11854","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11851","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11849","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11848","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11841","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11840","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11843","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11838","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11837","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11835","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11825","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11800","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11813","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11818","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11816","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11792","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11774","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11769","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11770","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11739","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=11714","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10705","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10703","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10600","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10599","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10597","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10594","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10592","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10591","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10583","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10580","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10575","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10560","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10533","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10516","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10521","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10522","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10520","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10517","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10493","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10487","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10479","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10448","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10444","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10446","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10354","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10331","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10332","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10318","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10315","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10317","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10301","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10306","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10302","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10303","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10304","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10305","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10300","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10294","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10291","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10289","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10287","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10286","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10285","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10284","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10276","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10246","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10169","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10164","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10161","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10111","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10110","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=10107","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8970","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8917","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8916","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8861","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8512","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8452","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8692","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8560","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8453","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8451","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8449","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8432","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8447","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8431","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8288","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8250","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8174","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8164","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8123","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=8008","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=7956","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=7912","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=7875","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=7874","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=7858","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=7856","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=7854","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=7846","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6750","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6714","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6705","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6701","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6651","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6590","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6576","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6510","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6507","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6506","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6329","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6305","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6245","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6231","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6222","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=6148","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5881","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5854","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5849","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5809","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5808","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5710","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5711","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5733","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5712","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5586","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5605","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5608","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5609","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5610","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5607","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5606","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5604","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5603","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5602","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5413","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5401","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5300","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5287","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5337","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5301","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5310","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5252","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5251","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5249","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5250","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5248","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5246","http://valleycenterhappenings.com/Admin/AddEditClassified.aspx?ClassifiedID=5247"]

        #edit_article_list = ["http://valleycenterhappenings.com/admin/AddEditClassified.aspx?ClassifiedID=11800"]

        for article_url in edit_article_list:
            article_edit_page = s.get(article_url, data=payload).text
            article_edit_soup = BeautifulSoup(article_edit_page, 'lxml')

            # Section
            for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvClassified$ddlSubMenu"}).findAll("option", {"selected":"selected"}):
                f.write(thing.get_text(strip=True) + "\t")

            # Category
            for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvClassified$ddlCategory"}).findAll("option", {"selected":"selected"}):
                f.write(thing.get_text(strip=True) + "\t")

            # Title
            for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvClassified$txtTitle"})['value']:
                for things in thing:
                    f.write(things)
            f.write("\t")

            # Body/Content
            for thing in article_edit_soup.findAll("textarea", {"name":"ctl00$ContentPlaceHolder1$fvClassified$txtClassifiedContent"}):
                thing1 = [re.sub('(\n)', '<br>', e) for e in thing.contents]
                thing2 = [re.sub('(\r|\t)', '', e) for e in thing1]
                thing3 = [re.sub('<br>', '', e) for e in thing2]
                for things in thing3:
                    if 'img src=' in things:
                        athing = things[:things.find(".jpg") + len(".jpg")]
                    f.write(things)
            f.write("\t")

            # Image
            if article_edit_soup.findAll("a", {"id":"ctl00_ContentPlaceHolder1_fvClassified_lnkViewImage"}) != None:
                for thing in article_edit_soup.findAll("a", {"id":"ctl00_ContentPlaceHolder1_fvClassified_lnkViewImage"}):
                    f.write(thing.get('onclick').replace("MyPopup('../Files/", "").replace("');return false;", ""))
            f.write("\t")

            # Featured Priority
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvClassified$txtPriority"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvClassified$txtPriority"})['value']:
                    f.write(thing)
            f.write("\t")

            # Scheduling Activate On
            for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvClassified$txtActivationDate"})['value']:
                f.write(thing)
            f.write("\t")

            # Scheduling Close On
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvClassified$txtClosingDate"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvClassified$txtClosingDate"})['value']:
                    f.write(thing)
            f.write("\t")

            # Flag
            for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvClassified$ddlFlag"}).findAll("option", {"selected":"selected"}):
                f.write(thing.get_text(strip=True) + "\t")

            # Status
            for thing in article_edit_soup.find_all("input", {"name":"ctl00_ContentPlaceHolder1_fvClassified_chkStatus", "checked":"checked"}):
                f.write("YES")
            f.write(os.linesep)



if __name__ == '__main__':
    main()

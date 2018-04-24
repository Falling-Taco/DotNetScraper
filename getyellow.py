from bs4 import BeautifulSoup
import requests
import re
import codecs
import os

#links needed
login_url = 'http://valleycenterhappenings.com/admin/'



def main():

    # file open and write
    f = codecs.open('yellowcompiled.txt', 'w+', encoding='utf-8')
    # headers
    f.write("Section\tCategory\tBusinness Name\tAddress\tCity\tState\tZip Code\tCountry\tFirst Name\tLast Name\tPhone\tEmail\tWebsite\tAbout\tImage\tCoupon\tFeatured Priority\tActivate On\tClose On\tComments\tFlag\tStatus")
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

        edit_article_list = ["http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6619","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=12185","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=12184","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=12177","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6612","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=12108","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6623","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=12066","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=12067","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6830","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=11756","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=11842","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=11757","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=11357","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6633","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=8164","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6631","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=11534","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6628","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=9498","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6624","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6634","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=9789","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6638","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7436","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7966","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7958","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7799","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6724","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7216","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6711","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7023","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6720","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6727","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6726","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6714","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6713","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6709","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6717","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6723","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6728","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6722","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6721","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6719","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6715","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6712","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6632","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7037","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6635","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7052","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7077","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7308","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6718","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7798","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7797","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7796","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6716","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6725","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=7045","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6626","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6707","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6636","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6613","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6618","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6625","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6637","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6639","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6630","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6621","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6622","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6615","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6708","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6620","http://valleycenterhappenings.com/Admin/AddEditDirectory.aspx?DirectoryID=6614"]



        for article_url in edit_article_list:
            article_edit_page = s.get(article_url, data=payload).text
            article_edit_soup = BeautifulSoup(article_edit_page, 'lxml')

            # Section
            if article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$ddlSubMenu"}) == None:
                continue
            else:
                for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$ddlSubMenu"}).findAll("option", {"selected":"selected"}):
                    f.write(thing.get_text(strip=True) + "\t")

            # Category
            for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$ddlCategory"}).findAll("option", {"selected":"selected"}):
                f.write(thing.get_text(strip=True))
            f.write("\t")

            # Business Name
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtCompanyName"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtCompanyName"})['value']:
                    f.write(thing)
            f.write("\t")

            # Address
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtAddress"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtAddress"})['value']:
                    f.write(thing)
            f.write("\t")

            # City
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtCity"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtCity"})['value']:
                    f.write(thing)
            f.write("\t")

            # State
            for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$ddlState"}).findAll("option", {"selected":"selected"}):
                f.write(thing.get_text(strip=True))
            f.write("\t")

            # Zip Code
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtPostalCode"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtPostalCode"})['value']:
                    f.write(thing)
            f.write("\t")

            # Country
            for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$ddlCountry"}).findAll("option", {"selected":"selected"}):
                f.write(thing.get_text(strip=True))
            f.write("\t")

            # First Name
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtFirstName"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtFirstName"})['value']:
                    f.write(thing)
            f.write("\t")

            # Last Name
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtLastName"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtLastName"})['value']:
                    f.write(thing)
            f.write("\t")

            # Phone
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtPhone"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtPhone"})['value']:
                    f.write(thing)
            f.write("\t")

            # Email
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtEmail"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtEmail"})['value']:
                    f.write(thing)
            f.write("\t")

            # Website
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtWebsite"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtWebsite"})['value']:
                    f.write(thing)
            f.write("\t")

            # About
            for thing in article_edit_soup.find("textarea", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtAbout"}):
                for things in thing:
                    things = things.strip("\t\r\n")
                    f.write(things)
            f.write("\t")

            # Image
            if article_edit_soup.findAll("a", {"id":"ctl00_ContentPlaceHolder1_fvDirectory_lnkViewImage"}) != None:
                for thing in article_edit_soup.findAll("a", {"id":"ctl00_ContentPlaceHolder1_fvDirectory_lnkViewImage"}):
                    f.write(thing.get('onclick').replace("MyPopup('../Files/", "").replace("');return false;", ""))
            f.write("\t")

            # Coupon
            if article_edit_soup.findAll("a", {"id":"ctl00_ContentPlaceHolder1_fvDirectory_lnkViewCouponsFile"}) != None:
                for thing in article_edit_soup.findAll("a", {"id":"ctl00_ContentPlaceHolder1_fvDirectory_lnkViewCouponsFile"}):
                    f.write(thing.get('onclick').replace("MyPopup('../Files/", "").replace("');return false;", ""))
            f.write("\t")

            # Featured  Priority
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtPriority"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtPriority"})['value']:
                    f.write(thing)
            f.write("\t")

            # Activate On
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtActivationDate"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtActivationDate"})['value']:
                    f.write(thing)
            f.write("\t")

            # Close On
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtClosingDate"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtClosingDate"})['value']:
                    f.write(thing)
            f.write("\t")

            # Comments
            if article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtComments"}).has_attr('value') == True:
                for thing in article_edit_soup.find("input", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$txtComments"})['value']:
                    f.write(thing)
            f.write("\t")

            # Flag
            for thing in article_edit_soup.find("select", {"name":"ctl00$ContentPlaceHolder1$fvDirectory$ddlFlag"}).findAll("option", {"selected":"selected"}):
                f.write(thing.get_text(strip=True))
            f.write("\t")

            # Status
            for thing in article_edit_soup.find_all("input", {"name":"ctl00_ContentPlaceHolder1_fvDirectory_chkStatus", "checked":"checked"}):
                f.write("YES")
            f.write(os.linesep)


if __name__ == '__main__':
    main()

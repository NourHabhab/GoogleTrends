#Importing Libraries 
import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
import hydralit_components as hc
from ast import keyword
from pytrends.request import TrendReq
from streamlit_lottie import st_lottie
import requests




#Layout 
st.set_page_config(layout="wide", page_icon = "https://cdn-icons-png.flaticon.com/512/2702/2702602.png", page_title = "Google Trends")
st.expander('Expander') 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


#creating menu data which will be used in navigation bar specifying the pages of the dashboard
menu_data = [
{'label':"Google"},
{'label':"1",'icon': "bi bi-google"},
{'label':"2",'icon': "bi bi-google"},
{'label':'3','icon': "bi bi-google"}]
over_theme = {'txc_inactive': 'white','menu_background':'rgb(180,151,231)', 'option_active':'white'}
#Updating layout Design and Layout 
menu_id = hc.nav_bar(menu_definition = menu_data,
                    sticky_mode = 'jumpy',
                    sticky_nav = True,
                    hide_streamlit_markers = False,
                    override_theme = {'txc_inactive': 'white',
                                        'menu_background' : '#4285F4',
                                        'txc_active':'#0178e4',
                                        'option_active':'white'})

#Editing First Page of automated scrapper 

if menu_id == "Google":
    #Installing an image 
    image = Image.open('1.PNG')
    row_spacer1, row_1, row_spacer2, row_2 = st.columns((.1, .1, .3, 1.8))
    with row_spacer1:
            st.image(image,width=300)
    with row_spacer2:
            st.empty()
    #Segmenting the page for the desired layout 
    
    # Display lottie animations
 
  
    col1,col2,col3=st.columns([1,2,1])
    with col2:
        st.markdown(f"""
            <h1>
                <h1 style="vertical-align:center;font-size:35px;padding-left:200px;color:#4285F4;padding-top:5px;margin-left:0em";>
                Explore what the world is searching
            </h1>""",unsafe_allow_html = True)
        
    col1,col2,col3,col4,col5,col6=st.columns([1,1.3,1,1,1,1])
    
    with col3:
        image1=Image.open('Capture1.PNG')
        st.image(image1,width=600)
        
    col1,col2,col3=st.columns([7,0.1,0.1])
    with col1:
        image1=Image.open('homecap.PNG')
        st.image(image1,width=1500)

#Editing Second Page of automated scrapper 
        
if menu_id == "1":
    image = Image.open('Capture6.PNG')

    row_spacer1, row_1, row_spacer2, row_2 = st.columns((.1, .1, .3, 1.8))
    with row_spacer1:
            st.image(image,width=400)
    with row_spacer2:
            st.empty()
            
    col=st.columns(2)
    with col[0]:
        def load_lottieurl(url):

                # get the url
            r = requests.get(url)
            # if error 200 raised return Nothing
            if r.status_code !=200:
                return None
            return r.json()
    
        lottie_google = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_xh83pj1c.json")
        st_lottie(lottie_google, key = "google", height = 300, width = 900)
    with col[1]:
        image1=Image.open('Chat1.PNG')
        st.image(image1,width=600)
    
   

   
    countries1={'United States':"US",'United Arab Emirates':"AE","Germany":"DE","Afghanistan":"AF",
                "Åland Islands":"AX","Albania":"AL","Algeria":"DZ","American Samoa":"AS","Andorra":"AD","Angola":"AO","Anguilla":"AI","Antarctica":"AQ","Argentina":"AR",
                "Armenia":"AM","Aruba":"AW","Australia":"AU","Austria":"AT","Azerbaijan":"AZ","Bahamas":"BS","Bahrain":"BH","Bangladesh":"BD","Barbados":"BB","Belarus":"BY",
                "Belgium":"BE","Belize":"BZ","Benin":"BJ","Bermuda":"BM","Bhutan":"BT","Bolivia":"BO","Botswana":"BW","Brazil":"BR","Brunei":"BN","Bulgaria":"BG","Burkina Faso":"BF",
                "Burundi":"BI","Cambodia":"KH","Cameroon":"CM","Canada":"CA","Cape Verde":"CV","Caribbean Netherlands":"BQ","Cayman Islands":"KY","Central African Republic":"CF",
                "Chad":"TD","Chile":"CL","China":"CN","Colombia":"CO","Costa Rica":"CR","Côte d’Ivoire":"CL","Croatia":"HR","Cyprus":"CY","Czechia":"CZ","Denmark":"DK","Djibouti":"DJ","Dominica":"DM",
                "Ecuador":"EC","Egypt":"EG","El Salvador":"SV","Equatorial Guinea":"GQ","Estonia":"EE","Eswatini":"SZ","Ethiopia":"ET","Faroe Islands":"FO","Fiji":"FJ","Finland":"FI","France":"FR","Gabon":"GA",
                "Gambia":"GM","Georgia":"GE","Ghana":"GH","Gibraltar":"GI","Greece":"GR","Grenada":"GD","Guadeloupe":"GP","Guatemala":"GT","Haiti":"HT","Honduras":"HN","Hong Kong":"HK","Hungary":"HU","Indonesia":"ID",
                "Iran":"IR","Iraq":"IQ","Ireland":"IE","Italy":"IT","Jamaica":"JM","Japan":"JP","Jersey":"JE","Jordan":"JO","Kazakhstan":"KZ","Kenya":"KE","Kosovo":"XK","Kuwait":"KW","Laos":"LA","Latvia":"LV","Lebanon":"LB",
                "Lesotho":"LS","Liberia":"LR","Libya":"LY","Liechtenstein":"LI","Lithuania":"LT","Luxembourg":"LU","Macao":"MO","Madagascar":"MG","Malawi":"MW","Malaysia":"MY","Maldives":"MV","Mali":"ML","Malta":"MT","Martinique":"MQ",
                "Mexico":"MX","Moldova":"MD","Mongolia":"MN","Montenegro":"ME","Morocco":"MA","Mozambique":"MZ","Namibia":"NA","Nepal":"NP","Netherlands":"NL","New Caledonia":"NC","New Zealand":"NZ","Nicaragua":"NI","Nigeria":"NG","Norway":"NO",
                "Oman":"OM","Pakistan":"PK","Palau":"PW","Palestine":"PS","Panama":"PA","Paraguay":"PY","Peru":"PE","Philippines":"PH","Poland":"PL","Portugal":"PT","Puerto Rico":"PR","Qatar":"QA","Réunion":"RE","Romania":"RO","Russia":"RU","Rwanda":"RW",
                "Saudi Arabia":"SA","Senegal":"SN","Serbia":"RS","Sierra Leone":"SL","Singapore":"SG","Sint Maarten":"SX","Slovakia":"SK","Slovenia":"SI","Somalia":"SO","South Africa":"ZA","South Korea":"KR","South Sudan":"SS",
                "Spain":"ES","Sri Lanka":"LK","Sudan":"SD","Suriname":"SR","Sweden":"SE","Switzerland":"CH","Syria":"SY","Taiwan":"TW","Tajikistan":"TJ","Tanzania":"TZ","Thailand":"TH","Togo":"TG","Tunisia":"TN","Turkey":"TR","Turkmenistan":"TM","Uganda":"UG",
                "Ukraine":"UA","United Kingdom":"GB","Uruguay":"UY","Uzbekistan":"UZ","Venezuela":"VE","Vietnam":"VN","Western Sahara":"EH","Yemen":"YE","Zambia":"ZM"}
    #Segmenting the page into three different columns for layout purpose 
    col1,col2,col3=st.columns(3)
    with col1:
                keyword2=st.text_input("Search Term")
                list2=[keyword2]
                
                # Customize Button
                button = st.markdown("""
                <style>
                div.stButton > button{
                background-color: #0178e4;
                color:#ffffff;
                box-shadow: #094c66 4px 4px 0px;
                border-radius:8px 8px 8px 8px;
                transition : transform 200ms,
                box-shadow 200ms;
                }
                div.stButton > button:focus{
                background-color: #0178e4;
                color:#ffffff;
                box-shadow: #094c66 4px 4px 0px;
                border-radius:8px 8px 8px 8px;
                transition : transform 200ms,
                box-shadow 200ms;
                }
                div.stButton > button:active {
                        transform : translateY(4px) translateX(4px);
                        box-shadow : #0178e4 0px 0px 0px;
                    }
                </style>""", unsafe_allow_html=True) 
                search=st.button("search")
    with col2:
            Choice=st.selectbox("Country",countries1)
    
    with col3:
        year=["Past 12 months","Past 5 years"]
        Choice1=st.selectbox("Time-Frame",year)
        
    #Initiating the scrapper    
    if search:
        if Choice1=="Past 5 years":
            for key in countries1.keys():
                if key==Choice:
                    pytrends=TrendReq(hl='en-Us') 
                    pytrends.build_payload(list2, 
                                    cat=0, 
                                    timeframe='today 5-y',
                                    geo=countries1[key], 
                                    gprop='')

                    d1  = pytrends.interest_over_time()
                    d1.to_csv('MTrends.csv')
                    df1=pd.read_csv("MTrends.csv")
                    df1['date'] = pd.to_datetime(df1['date'])
                    df1['date'] = df1['date'].apply(lambda row: row.year)
                    pivot1 = df1.pivot_table(index=['date'], values=list2, aggfunc='mean')
                    pivot1=pivot1.reset_index(drop = False)
                    fig2 = px.line(pivot1, x="date", y=pivot1.iloc[:,1])
                    fig2.update_xaxes(showgrid=False)
                    fig2.update_yaxes(showgrid=False)

                    st.plotly_chart(fig2, use_container_width=True)
        
        if Choice1=="Past 12 months":
            for key in countries1.keys():
                if key==Choice:
                    pytrends=TrendReq(hl='en-Us') 
                    pytrends.build_payload(list2, 
                                    cat=0, 
                                    timeframe='today 12-m',
                                    geo=countries1[key], 
                                    gprop='')

                    d1  = pytrends.interest_over_time()
                    d1.to_csv('MTrends.csv')
                    df1=pd.read_csv("MTrends.csv")
                    df1['date'] = pd.to_datetime(df1['date'])
                    fig2 = px.line(df1, x="date", y=df1.iloc[:,1])
                    fig2.update_xaxes(showgrid=False)
                    fig2.update_yaxes(showgrid=False)
                    st.plotly_chart(fig2, use_container_width=True)

#Editing Third Page of automated scrapper   
if menu_id == "3":
    image = Image.open('Capture6.PNG')

    row_spacer1, row_1, row_spacer2, row_2 = st.columns((.1, .1, .3, 1.8))
    with row_spacer1:
            st.image(image,width=400)
    with row_spacer2:
            st.empty()
    col=st.columns(2)
    with col[0]:
        def load_lottieurl(url):

                # get the url
            r = requests.get(url)
            # if error 200 raised return Nothing
            if r.status_code !=200:
                return None
            return r.json()
    
        lottie_google = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_uetcyfgk.json")
        st_lottie(lottie_google, key = "google", height = 300, width = 900)
    with col[1]:
        image1=Image.open('Chat2.PNG')
        st.image(image1,width=600)
    

  
    
    #This is a dictonary representing the code of the geoloction in google trends 
    
    countries1={'United States':"US",'United Arab Emirates':"AE","Germany":"DE","Afghanistan":"AF",
                "Åland Islands":"AX","Albania":"AL","Algeria":"DZ","American Samoa":"AS","Andorra":"AD","Angola":"AO","Anguilla":"AI","Antarctica":"AQ","Argentina":"AR",
                "Armenia":"AM","Aruba":"AW","Australia":"AU","Austria":"AT","Azerbaijan":"AZ","Bahamas":"BS","Bahrain":"BH","Bangladesh":"BD","Barbados":"BB","Belarus":"BY",
                "Belgium":"BE","Belize":"BZ","Benin":"BJ","Bermuda":"BM","Bhutan":"BT","Bolivia":"BO","Botswana":"BW","Brazil":"BR","Brunei":"BN","Bulgaria":"BG","Burkina Faso":"BF",
                "Burundi":"BI","Cambodia":"KH","Cameroon":"CM","Canada":"CA","Cape Verde":"CV","Caribbean Netherlands":"BQ","Cayman Islands":"KY","Central African Republic":"CF",
                "Chad":"TD","Chile":"CL","China":"CN","Colombia":"CO","Costa Rica":"CR","Côte d’Ivoire":"CL","Croatia":"HR","Cyprus":"CY","Czechia":"CZ","Denmark":"DK","Djibouti":"DJ","Dominica":"DM",
                "Ecuador":"EC","Egypt":"EG","El Salvador":"SV","Equatorial Guinea":"GQ","Estonia":"EE","Eswatini":"SZ","Ethiopia":"ET","Faroe Islands":"FO","Fiji":"FJ","Finland":"FI","France":"FR","Gabon":"GA",
                "Gambia":"GM","Georgia":"GE","Ghana":"GH","Gibraltar":"GI","Greece":"GR","Grenada":"GD","Guadeloupe":"GP","Guatemala":"GT","Haiti":"HT","Honduras":"HN","Hong Kong":"HK","Hungary":"HU","Indonesia":"ID",
                "Iran":"IR","Iraq":"IQ","Ireland":"IE","Italy":"IT","Jamaica":"JM","Japan":"JP","Jersey":"JE","Jordan":"JO","Kazakhstan":"KZ","Kenya":"KE","Kosovo":"XK","Kuwait":"KW","Laos":"LA","Latvia":"LV","Lebanon":"LB",
                "Lesotho":"LS","Liberia":"LR","Libya":"LY","Liechtenstein":"LI","Lithuania":"LT","Luxembourg":"LU","Macao":"MO","Madagascar":"MG","Malawi":"MW","Malaysia":"MY","Maldives":"MV","Mali":"ML","Malta":"MT","Martinique":"MQ",
                "Mexico":"MX","Moldova":"MD","Mongolia":"MN","Montenegro":"ME","Morocco":"MA","Mozambique":"MZ","Namibia":"NA","Nepal":"NP","Netherlands":"NL","New Caledonia":"NC","New Zealand":"NZ","Nicaragua":"NI","Nigeria":"NG","Norway":"NO",
                "Oman":"OM","Pakistan":"PK","Palau":"PW","Palestine":"PS","Panama":"PA","Paraguay":"PY","Peru":"PE","Philippines":"PH","Poland":"PL","Portugal":"PT","Puerto Rico":"PR","Qatar":"QA","Réunion":"RE","Romania":"RO","Russia":"RU","Rwanda":"RW",
                "Saudi Arabia":"SA","Senegal":"SN","Serbia":"RS","Sierra Leone":"SL","Singapore":"SG","Sint Maarten":"SX","Slovakia":"SK","Slovenia":"SI","Somalia":"SO","South Africa":"ZA","South Korea":"KR","South Sudan":"SS",
                "Spain":"ES","Sri Lanka":"LK","Sudan":"SD","Suriname":"SR","Sweden":"SE","Switzerland":"CH","Syria":"SY","Taiwan":"TW","Tajikistan":"TJ","Tanzania":"TZ","Thailand":"TH","Togo":"TG","Tunisia":"TN","Turkey":"TR","Turkmenistan":"TM","Uganda":"UG",
                "Ukraine":"UA","United Kingdom":"GB","Uruguay":"UY","Uzbekistan":"UZ","Venezuela":"VE","Vietnam":"VN","Western Sahara":"EH","Yemen":"YE","Zambia":"ZM"}

    countries2={'United States':"US",'United Arab Emirates':"AE","Germany":"DE","Afghanistan":"AF",
                "Åland Islands":"AX","Albania":"AL","Algeria":"DZ","American Samoa":"AS","Andorra":"AD","Angola":"AO","Anguilla":"AI","Antarctica":"AQ","Argentina":"AR",
                "Armenia":"AM","Aruba":"AW","Australia":"AU","Austria":"AT","Azerbaijan":"AZ","Bahamas":"BS","Bahrain":"BH","Bangladesh":"BD","Barbados":"BB","Belarus":"BY",
                "Belgium":"BE","Belize":"BZ","Benin":"BJ","Bermuda":"BM","Bhutan":"BT","Bolivia":"BO","Botswana":"BW","Brazil":"BR","Brunei":"BN","Bulgaria":"BG","Burkina Faso":"BF",
                "Burundi":"BI","Cambodia":"KH","Cameroon":"CM","Canada":"CA","Cape Verde":"CV","Caribbean Netherlands":"BQ","Cayman Islands":"KY","Central African Republic":"CF",
                "Chad":"TD","Chile":"CL","China":"CN","Colombia":"CO","Costa Rica":"CR","Côte d’Ivoire":"CL","Croatia":"HR","Cyprus":"CY","Czechia":"CZ","Denmark":"DK","Djibouti":"DJ","Dominica":"DM",
                "Ecuador":"EC","Egypt":"EG","El Salvador":"SV","Equatorial Guinea":"GQ","Estonia":"EE","Eswatini":"SZ","Ethiopia":"ET","Faroe Islands":"FO","Fiji":"FJ","Finland":"FI","France":"FR","Gabon":"GA",
                "Gambia":"GM","Georgia":"GE","Ghana":"GH","Gibraltar":"GI","Greece":"GR","Grenada":"GD","Guadeloupe":"GP","Guatemala":"GT","Haiti":"HT","Honduras":"HN","Hong Kong":"HK","Hungary":"HU","Indonesia":"ID",
                "Iran":"IR","Iraq":"IQ","Ireland":"IE","Italy":"IT","Jamaica":"JM","Japan":"JP","Jersey":"JE","Jordan":"JO","Kazakhstan":"KZ","Kenya":"KE","Kosovo":"XK","Kuwait":"KW","Laos":"LA","Latvia":"LV","Lebanon":"LB",
                "Lesotho":"LS","Liberia":"LR","Libya":"LY","Liechtenstein":"LI","Lithuania":"LT","Luxembourg":"LU","Macao":"MO","Madagascar":"MG","Malawi":"MW","Malaysia":"MY","Maldives":"MV","Mali":"ML","Malta":"MT","Martinique":"MQ",
                "Mexico":"MX","Moldova":"MD","Mongolia":"MN","Montenegro":"ME","Morocco":"MA","Mozambique":"MZ","Namibia":"NA","Nepal":"NP","Netherlands":"NL","New Caledonia":"NC","New Zealand":"NZ","Nicaragua":"NI","Nigeria":"NG","Norway":"NO",
                "Oman":"OM","Pakistan":"PK","Palau":"PW","Palestine":"PS","Panama":"PA","Paraguay":"PY","Peru":"PE","Philippines":"PH","Poland":"PL","Portugal":"PT","Puerto Rico":"PR","Qatar":"QA","Réunion":"RE","Romania":"RO","Russia":"RU","Rwanda":"RW",
                "Saudi Arabia":"SA","Senegal":"SN","Serbia":"RS","Sierra Leone":"SL","Singapore":"SG","Sint Maarten":"SX","Slovakia":"SK","Slovenia":"SI","Somalia":"SO","South Africa":"ZA","South Korea":"KR","South Sudan":"SS",
                "Spain":"ES","Sri Lanka":"LK","Sudan":"SD","Suriname":"SR","Sweden":"SE","Switzerland":"CH","Syria":"SY","Taiwan":"TW","Tajikistan":"TJ","Tanzania":"TZ","Thailand":"TH","Togo":"TG","Tunisia":"TN","Turkey":"TR","Turkmenistan":"TM","Uganda":"UG",
                "Ukraine":"UA","United Kingdom":"GB","Uruguay":"UY","Uzbekistan":"UZ","Venezuela":"VE","Vietnam":"VN","Western Sahara":"EH","Yemen":"YE","Zambia":"ZM"}
    
    col1,col2,col3,col4=st.columns(4)
    with col1:
        word=st.text_input("Search Term")
        list=[word]
    with col2:
        Choice2=st.selectbox("Country",countries1)
    with col3:
        Choice3=st.selectbox("Country2",countries2)
    with col4:
        year=["Past 12 months","Past 5 years"]
        Choice1=st.selectbox("Time-Frame",year)
        
        
      # Customize Button
    button = st.markdown("""
                <style>
                div.stButton > button{
                background-color: #0178e4;
                color:#ffffff;
                box-shadow: #094c66 4px 4px 0px;
                border-radius:8px 8px 8px 8px;
                transition : transform 200ms,
                box-shadow 200ms;
                }
                div.stButton > button:focus{
                background-color: #0178e4;
                color:#ffffff;
                box-shadow: #094c66 4px 4px 0px;
                border-radius:8px 8px 8px 8px;
                transition : transform 200ms,
                box-shadow 200ms;
                }
                div.stButton > button:active {
                        transform : translateY(4px) translateX(4px);
                        box-shadow : #0178e4 0px 0px 0px;
                    }
                </style>""", unsafe_allow_html=True) 
    search=st.button("search")
    
    #Intiating the scrapper 
    if word:
        if Choice1=="Past 5 years":

            for key in countries1.keys():
                if key==Choice2:
                
                    pytrends=TrendReq(hl='en-Us') 
                
                    pytrends.build_payload(list, 
                                    cat=0, 
                                    timeframe='today 5-y',
                                    geo=countries1[key], 
                                    gprop='')

                    d  = pytrends.interest_over_time()
                    d.to_csv('KTrends.csv')
                    df=pd.read_csv("KTrends.csv")
                    df['date'] = pd.to_datetime(df['date'])
                    df['date'] = df['date'].apply(lambda row: row.year)
                    pivot = df.pivot_table(index=['date'], values=list, aggfunc='mean')
                    pivot=pivot.reset_index(drop = False)
                    
                
            for key in countries2.keys():
                if key==Choice3:
                    
                    pytrends=TrendReq(hl='en-Us') 
                
                    pytrends.build_payload(list, 
                                    cat=0, 
                                    timeframe='today 5-y',
                                    geo=countries2[key], 
                                    gprop='')

                    d  = pytrends.interest_over_time()
                    d.to_csv('NTrends.csv')
                    df2=pd.read_csv("NTrends.csv")
                    df2['date'] = pd.to_datetime(df2['date'])
                    df2['date'] = df2['date'].apply(lambda row: row.year)
                    pivot1 = df2.pivot_table(index=['date'], values=list, aggfunc='mean')
                    pivot1=pivot1.reset_index(drop = False)
                    pivot1.columns.values[1] = "Country2"
                    pivot1=pivot1.drop(["date"],axis=1)
                    horizontal_concat = pd.concat([pivot, pivot1], axis=1)
                    df3=pd.DataFrame(horizontal_concat)
                    columns=df3.columns
                    df4=pd.melt(df3, id_vars =['date'], value_vars =[columns[1], columns[2]],
                                                                    var_name ='keyword')
                    columns1=df4.columns
                    fig3 = px.line(df4, x="date", y=columns1[2],color=columns1[1])
                    fig3.update_xaxes(showgrid=False)
                    fig3.update_yaxes(showgrid=False)
                    st.plotly_chart(fig3, use_container_width=True)
                    
        if Choice1=="Past 12 months":
            
            for key in countries1.keys():
                if key==Choice2:
                
                    pytrends=TrendReq(hl='en-Us') 
                
                    pytrends.build_payload(list, 
                                    cat=0, 
                                    timeframe='today 12-m',
                                    geo=countries1[key], 
                                    gprop='')

                    d  = pytrends.interest_over_time()
                    d.to_csv('cTrends.csv')
                    df=pd.read_csv("cTrends.csv")
                    df['date'] = pd.to_datetime(df['date'])
                    
                
                    
            for key in countries2.keys():
                if key==Choice3:
                    st.header(countries2[key])
                    st.header(type(countries2[key]))
                    pytrends=TrendReq(hl='en-Us') 
                    pytrends.build_payload(list, 
                                    cat=0, 
                                    timeframe='today 12-m',
                                    geo=countries2[key], 
                                    gprop='')

                    d  = pytrends.interest_over_time()
                    d.to_csv('MTrends.csv')
                    df2=pd.read_csv("MTrends.csv")
                    df2['date'] = pd.to_datetime(df2['date'])
                    
                    df2=df2.drop(["isPartial"],axis=1)
                    df2.columns.values[1] = "Line2"
                    df2=df2.drop(["date"],axis=1)
                    horizontal_concat = pd.concat([df,df2], axis=1)
                    df3=pd.DataFrame(horizontal_concat)
                    df3=df3.drop(["isPartial"],axis=1)
                    columns=df3.columns
                    df4=pd.melt(df3, id_vars =['date'], value_vars =[columns[1], columns[2]],
                                                                    var_name ='keyword')
                    columns1=df4.columns
                    fig3 = px.line(df4, x="date", y=columns1[2],color=columns1[1])
                    fig3.update_xaxes(showgrid=False)
                    fig3.update_yaxes(showgrid=False)
                    st.plotly_chart(fig3, use_container_width=True)

#Editing Fourth Page of automated scrapper  
if menu_id=="2": 
    image = Image.open('Capture6.PNG')

    row_spacer1, row_1, row_spacer2, row_2 = st.columns((.1, .1, .3, 1.8))
    with row_spacer1:
            st.image(image,width=400)
    with row_spacer2:
            st.empty()
    
    col=st.columns(2)
    with col[0]:
        def load_lottieurl(url):

                # get the url
            r = requests.get(url)
            # if error 200 raised return Nothing
            if r.status_code !=200:
                return None
            return r.json()
    
        lottie_google = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_xh83pj1c.json")
        st_lottie(lottie_google, key = "google", height = 300, width = 900)
    with col[1]:
        image1=Image.open('Chat3.PNG')
        st.image(image1,width=600)

    
   
    
        
    pytrends=TrendReq(hl='en-Us')    
    placeholder=st.empty()
    countries1={'United States':"US",'United Arab Emirates':"AE","Germany":"DE","Afghanistan":"AF",
                "Åland Islands":"AX","Albania":"AL","Algeria":"DZ","American Samoa":"AS","Andorra":"AD","Angola":"AO","Anguilla":"AI","Antarctica":"AQ","Argentina":"AR",
                "Armenia":"AM","Aruba":"AW","Australia":"AU","Austria":"AT","Azerbaijan":"AZ","Bahamas":"BS","Bahrain":"BH","Bangladesh":"BD","Barbados":"BB","Belarus":"BY",
                "Belgium":"BE","Belize":"BZ","Benin":"BJ","Bermuda":"BM","Bhutan":"BT","Bolivia":"BO","Botswana":"BW","Brazil":"BR","Brunei":"BN","Bulgaria":"BG","Burkina Faso":"BF",
                "Burundi":"BI","Cambodia":"KH","Cameroon":"CM","Canada":"CA","Cape Verde":"CV","Caribbean Netherlands":"BQ","Cayman Islands":"KY","Central African Republic":"CF",
                "Chad":"TD","Chile":"CL","China":"CN","Colombia":"CO","Costa Rica":"CR","Côte d’Ivoire":"CL","Croatia":"HR","Cyprus":"CY","Czechia":"CZ","Denmark":"DK","Djibouti":"DJ","Dominica":"DM",
                "Ecuador":"EC","Egypt":"EG","El Salvador":"SV","Equatorial Guinea":"GQ","Estonia":"EE","Eswatini":"SZ","Ethiopia":"ET","Faroe Islands":"FO","Fiji":"FJ","Finland":"FI","France":"FR","Gabon":"GA",
                "Gambia":"GM","Georgia":"GE","Ghana":"GH","Gibraltar":"GI","Greece":"GR","Grenada":"GD","Guadeloupe":"GP","Guatemala":"GT","Haiti":"HT","Honduras":"HN","Hong Kong":"HK","Hungary":"HU","Indonesia":"ID",
                "Iran":"IR","Iraq":"IQ","Ireland":"IE","Italy":"IT","Jamaica":"JM","Japan":"JP","Jersey":"JE","Jordan":"JO","Kazakhstan":"KZ","Kenya":"KE","Kosovo":"XK","Kuwait":"KW","Laos":"LA","Latvia":"LV","Lebanon":"LB",
                "Lesotho":"LS","Liberia":"LR","Libya":"LY","Liechtenstein":"LI","Lithuania":"LT","Luxembourg":"LU","Macao":"MO","Madagascar":"MG","Malawi":"MW","Malaysia":"MY","Maldives":"MV","Mali":"ML","Malta":"MT","Martinique":"MQ",
                "Mexico":"MX","Moldova":"MD","Mongolia":"MN","Montenegro":"ME","Morocco":"MA","Mozambique":"MZ","Namibia":"NA","Nepal":"NP","Netherlands":"NL","New Caledonia":"NC","New Zealand":"NZ","Nicaragua":"NI","Nigeria":"NG","Norway":"NO",
                "Oman":"OM","Pakistan":"PK","Palau":"PW","Palestine":"PS","Panama":"PA","Paraguay":"PY","Peru":"PE","Philippines":"PH","Poland":"PL","Portugal":"PT","Puerto Rico":"PR","Qatar":"QA","Réunion":"RE","Romania":"RO","Russia":"RU","Rwanda":"RW",
                "Saudi Arabia":"SA","Senegal":"SN","Serbia":"RS","Sierra Leone":"SL","Singapore":"SG","Sint Maarten":"SX","Slovakia":"SK","Slovenia":"SI","Somalia":"SO","South Africa":"ZA","South Korea":"KR","South Sudan":"SS",
                "Spain":"ES","Sri Lanka":"LK","Sudan":"SD","Suriname":"SR","Sweden":"SE","Switzerland":"CH","Syria":"SY","Taiwan":"TW","Tajikistan":"TJ","Tanzania":"TZ","Thailand":"TH","Togo":"TG","Tunisia":"TN","Turkey":"TR","Turkmenistan":"TM","Uganda":"UG",
                "Ukraine":"UA","United Kingdom":"GB","Uruguay":"UY","Uzbekistan":"UZ","Venezuela":"VE","Vietnam":"VN","Western Sahara":"EH","Yemen":"YE","Zambia":"ZM"}
    
    col1,col2,col3,col4=st.columns(4)
    with col1:    
            keyword=st.text_input("Search Term")
            list=[keyword]
    with col2:
            keyword2=st.text_input("+ Compare")
            list2=[keyword2]
    with col3:   
            Choice=st.selectbox("Country",countries1)
    with col4:
        year=["Past 12 months","Past 5 years"]
        Choice1=st.selectbox("Time-Frame",year)
        
    
    # Customize Button
    button = st.markdown("""
                <style>
                div.stButton > button{
                background-color: #0178e4;
                color:#ffffff;
                box-shadow: #094c66 4px 4px 0px;
                border-radius:8px 8px 8px 8px;
                transition : transform 200ms,
                box-shadow 200ms;
                }
                div.stButton > button:focus{
                background-color: #0178e4;
                color:#ffffff;
                box-shadow: #094c66 4px 4px 0px;
                border-radius:8px 8px 8px 8px;
                transition : transform 200ms,
                box-shadow 200ms;
                }
                div.stButton > button:active {
                        transform : translateY(4px) translateX(4px);
                        box-shadow : #0178e4 0px 0px 0px;
                    }
                </style>""", unsafe_allow_html=True) 
    search=st.button("search")

        
    #Initiating the scrapper         
    if search:
        if Choice1=="Past 5 years":
            
            for key in countries1.keys():
                if key==Choice:
                    pytrends.build_payload(list, 
                                    cat=0, 
                                    timeframe='today 5-y',
                                    geo=countries1[key], 
                                    gprop='')
            

                    d  = pytrends.interest_over_time()
                    d.to_csv('cTrends.csv')
                    df=pd.read_csv("cTrends.csv")
                    df['date'] = pd.to_datetime(df['date'])
                    df['date'] = df['date'].apply(lambda row: row.year)
                    pivot = df.pivot_table(index=['date'], values=list, aggfunc='mean')
                    pivot=pivot.reset_index(drop = False)
                    
                
            for key in countries1.keys():
                if key==Choice:
                    pytrends.build_payload(list2, 
                                    cat=0, 
                                    timeframe='today 5-y',
                                    geo=countries1[key], 
                                    gprop='')
            
                

                    d1  = pytrends.interest_over_time()
                    d1.to_csv('MTrends.csv')
                    df1=pd.read_csv("MTrends.csv")
                    df1['date'] = pd.to_datetime(df1['date'])
                    df1['date'] = df1['date'].apply(lambda row: row.year)
                    pivot1 = df1.pivot_table(index=['date'], values=list2, aggfunc='mean')
                    pivot1=pivot1.reset_index(drop = False)
                    pivot1=pivot1.drop(["date"],axis=1)
                    horizontal_concat = pd.concat([pivot, pivot1], axis=1)
                    df3=pd.DataFrame(horizontal_concat)
                    columns=df3.columns
                    df4=pd.melt(df3, id_vars =['date'], value_vars =[columns[1], columns[2]],
                                                                    var_name ='keyword')
                    columns1=df4.columns
                    fig4 = px.line(df4, x="date", y=columns1[2],color=columns1[1])
                    fig4.update_xaxes(showgrid=False)
                    fig4.update_yaxes(showgrid=False)
                    st.plotly_chart(fig4, use_container_width=True)
        
        if Choice1=="Past 12 months":
            
            for key in countries1.keys():
                if key==Choice:
                    pytrends=TrendReq(hl='en-Us') 
                    pytrends.build_payload(list, 
                                    cat=0, 
                                    timeframe='today 12-m',
                                    geo=countries1[key], 
                                    gprop='')

                    d  = pytrends.interest_over_time()
                    d.to_csv('cTrends.csv')
                    df=pd.read_csv("cTrends.csv")
                    df['date'] = pd.to_datetime(df['date'])
                
                    
            for key in countries1.keys():
                if key==Choice:
                    pytrends=TrendReq(hl='en-Us') 
                    pytrends.build_payload(list2, 
                                    cat=0, 
                                    timeframe='today 12-m',
                                    geo=countries1[key], 
                                    gprop='')

                    d  = pytrends.interest_over_time()
                    d.to_csv('MTrends.csv')
                    df2=pd.read_csv("MTrends.csv")
                    df2['date'] = pd.to_datetime(df2['date'])
                    
                    df2=df2.drop(["isPartial"],axis=1)
                    df2=df2.drop(["date"],axis=1)
                    horizontal_concat = pd.concat([df,df2], axis=1)
                    df3=pd.DataFrame(horizontal_concat)
                    df3=df3.drop(["isPartial"],axis=1)
                    columns=df3.columns
                    df4=pd.melt(df3, id_vars =['date'], value_vars =[columns[1], columns[2]],
                                                                    var_name ='keyword')
                    columns1=df4.columns
                    fig3 = px.line(df4, x="date", y=columns1[2],color=columns1[1])
                    fig3.update_xaxes(showgrid=False)
                    fig3.update_yaxes(showgrid=False)
                    st.plotly_chart(fig3, use_container_width=True)

import requests
from bs4 import BeautifulSoup
import pandas as pd

"""
we want to scrape data for used boats listings
for each brand (e.g:AB inflatables) we go throgh listings and for each listing properties of the boat is scraped
listings for each brand is stored in a seperate file
"""

# first request to get list of brands(makes)
req=requests.get(r'https://www.boatsonline.com.au/')
bs=BeautifulSoup(req.text,'html.parser')
makes=bs.find(id="Make_Model").find_all('option')[1:]
# iterating over brands (make = brand)
for make in makes:

    #make should be adjusted to fit url encoding tructure(AB inflatables --> AB-inflatables)
    make=make['value'].replace(' ','-')
    #initial request for make and load listings in first page()
    url=r'https://www.boatsonline.com.au/boats-for-sale/'+make+r'/used/?action=adv_search&listed=Anytime&keywords=&hull_material=All&Lengthfrom=&Lengthto=&feetfrom=&feetto=&price_from=1&price_to=1000000000&poa=yes&yearfrom=&yearto=&order_by=added_desc&pge=1'
    req=requests.get(url)
    bs=BeautifulSoup(req.text,'html.parser')
    # store every property in listing as a list consecutively
    Model=[]
    Make=[]
    Status=[]
    Name=[]
    Price=[]
    Image=[]
    Length=[]
    Use=[]
    Location=[]
    Launch_Year=[]
    Hull=[]
    Region=[]
    Displacement=[]
    Keel_Ballast=[]
    Decks_Material=[]
    Beam=[]
    Draft=[]
    Registration=[]
    Rego_Expiry=[]
    Engine_Make=[]
    Engine=[]
    Number_Engines=[]
    Horse_Power=[]
    Fuel_Type=[]
    Engine_Hours=[]
    Fuel_Consumption=[]
    Propulsion=[]
    Max_Speed=[]
    Cruise_Speed=[]
    Genset=[]
    Fuel=[]
    Water=[]
    Dinghy=[]
    Outboard=[]
    Covers=[]
    Berths=[]
    Shower=[]
    Toilet=[]
    Entertainment=[]
    Galley=[]
    Refrigeration=[]
    Freezer=[]
    Water_Maker=[]
    Mast_Rigging=[]
    Stove=[]
    Hot_Water=[]
    Safety_Gear=[]
    Sail_Inventory=[]
    Deck_Gear=[]
    Bilge_Pumps=[]
    Fire_Protection=[]
    Life_Raft=[]
    Life_Jackets=[]
    Accommodation=[]
    Air_Conditioning=[]
    Electrics=[]
    Electronics_Navigation=[]
    Broker_Dealer=[]
    Telephone=[]
    Address=[]
    City_Suburb=[]
    State=[]
    Country=[]
    Website=[]
    Url=[]

    boats=bs.find_all(class_="article listing-container").
    # iterate over boats and request properties for every boat
    while boats:
    
        for boat in boats:
            f_url=r'https://www.boatsonline.com.au'+boat.a['href']
            req=requests.get(f_url)
            boat=BeautifulSoup(req.text,'html.parser')
            try:
                Status.append(boat.find(class_="btn btn-lg btn-danger").text)
            except:
                try:
                    Status.append(boat.find(class_="btn btn-md btn-warning").text)
                except:
                    Status.append("")
            Name.append(boat.find(class_="h3 margin-top-sm").text.strip())       
            Make.append(make['value'])
            Model.append(boat.find_all(class_="h5 inline")[1].text)
            try:
                Price.append(list(boat.find(class_='row Boat_Header_Field_Row Boat_Price').find(class_="col-sm-9 Field").strings)[0].strip())
            except:
                Price.append('')
            try:
                Image.append(boat.find('img')['src'].strip())
            except:
                Image.append('')
            try:
                Length.append(boat.find(class_="row Boat_Header_Field_Row Boat_Length").find(class_="col-sm-9 Field").text.strip())
            except:
                Length.append('')
            try:
                Use.append(boat.find(class_="row Boat_Header_Field_Row Boat_Usage").find(class_="col-sm-9 Field").text.strip())
            except:
                Use.append('')
            try:
                Location.append(boat.find(class_="row Boat_Header_Field_Row Boat_Location").find(class_="col-sm-9 Field").text.strip())
            except:
                Location.append('')
            try:
                Launch_Year.append(boat.find(class_="row Boat_Header_Field_Row Boat_Year").find(class_="col-sm-9 Field").text.strip())
            except:
                Launch_Year.append('')
            try:
                Hull.append(boat.find(class_="row Boat_Header_Field_Row Boat_HullMaterial").find(class_="col-sm-9 Field").text.strip())
            except:
                Hull.append('')
            try:
                Region.append(boat.find(class_="row Boat_Field_Row Boat_Region").find_all('div')[-1].text.strip())
            except:
                Region.append('')
            try:
                Displacement.append(boat.find(class_="row Boat_Field_Row Boat_Displacement").find_all('div')[-1].text)
            except:
                Displacement.append('')
            try:
                Keel_Ballast.append(boat.find(class_="row Boat_Field_Row Boat_Ballast").find_all('div')[-1].text.strip())
            except:
                Keel_Ballast.append('')
            try:
                Decks_Material.append(boat.find(class_="row Boat_Field_Row Boat_DecksMaterial").find_all('div')[-1].text.strip())
            except:
                Decks_Material.append('')
            try:
                Beam.append(boat.find(class_="row Boat_Field_Row Boat_Beam").find_all('div')[-1].text)
            except:
                Beam.append('')
            try:
                Draft.append(boat.find(class_="row Boat_Field_Row Boat_Draft").find_all('div')[-1].text)
            except:
                Draft.append('')
            try:
                Registration.append(boat.find(class_="row Boat_Field_Row Boat_RegistrationNumber").find_all('div')[-1].text)
            except:
                Registration.append('')
            try:
                Rego_Expiry.append(boat.find(class_="row Boat_Field_Row Boat_RegistrationExpiry").find_all('div')[-1].text)
            except:
                Rego_Expiry.append('')
            try:
                Engine_Make.append(boat.find(class_="row Boat_Field_Row Boat_EngineMake").find_all('div')[-1].text)
            except:
                Engine_Make.append('')
            try:
                Engine.append(boat.find(class_="row Boat_Field_Row Boat_Engine").find_all('div')[-1].text)
            except:
                Engine.append('')
            try:
                Number_Engines.append(boat.find(class_="row Boat_Field_Row Boat_NumberEngines").find_all('div')[-1].text)
            except:
                Number_Engines.append('')
            try:
                Horse_Power.append(boat.find(class_="row Boat_Field_Row Boat_HorsePower").find_all('div')[-1].text)
            except:
                Horse_Power.append('')
            try:
                Fuel_Type.append(boat.find(class_="row Boat_Field_Row Boat_FuelType").find_all('div')[-1].text)
            except:
                Fuel_Type.append('')
            try:
                Engine_Hours.append(boat.find(class_="row Boat_Field_Row Boat_EngineHours").find_all('div')[-1].text)
            except:
                Engine_Hours.append('')
            try:
                Fuel_Consumption.append(boat.find(class_="row Boat_Field_Row Boat_FuelConsumption").find_all('div')[-1].text)
            except:
                Fuel_Consumption.append('')
            try:
                Propulsion.append(boat.find(class_="row Boat_Field_Row Boat_Propulsion").find_all('div')[-1].text)
            except:
                Propulsion.append('')
            try:
                Max_Speed.append(boat.find(class_="row Boat_Field_Row Boat_MaxSpeed").find_all('div')[-1].text.strip())
            except:
                Max_Speed.append('')
            try:
                Cruise_Speed.append(boat.find(class_="col-sm-2 Label Boat_CruiseSpeed_Label").find_all('div')[-1].text.strip())
            except:
                Cruise_Speed.append('')
            try:
                Genset.append(boat.find(class_="row Boat_Field_Row Boat_Genset").find_all('div')[-1].text)
            except:
                Genset.append('')
            try:
                Fuel.append(boat.find(class_="row Boat_Field_Row Boat_Fuel").find_all('div')[-1].text)
            except:
                Fuel.append('')
            try:
                Water.append(boat.find(class_="row Boat_Field_Row Boat_Water").find_all('div')[-1].text)
            except:
                Water.append('')
            try:
                Dinghy.append(boat.find(class_="row Boat_Field_Row Boat_Dinghy").find_all('div')[-1].text)
            except:
                Dinghy.append('')
            try:
                Outboard.append(boat.find(class_="row Boat_Field_Row Boat_Outboard").find_all('div')[-1].text)
            except:
                Outboard.append('')
            try:
                Covers.append(boat.find(class_="row Boat_Field_Row Boat_Covers").find_all('div')[-1].text)
            except:
                Covers.append('')
            try:
                Berths.append(boat.find(class_="row Boat_Field_Row Boat_Berths").find_all('div')[-1].text.strip())
            except:
                Berths.append('')
            try:
                Shower.append(boat.find(class_="row Boat_Field_Row Boat_Shower").find_all('div')[-1].text)
            except:
                Shower.append('')
            try:
                Toilet.append(boat.find(class_="row Boat_Field_Row Boat_Toilet").find_all('div')[-1].text)
            except:
                Toilet.append('')
            try:
                Entertainment.append(boat.find(class_="row Boat_Field_Row Boat_Entertainment").find_all('div')[-1].text.strip())
            except:
                Entertainment.append('')
            try:
                Galley.append(boat.find(class_="row Boat_Field_Row Boat_Galley").find_all('div')[-1].text.strip())
            except:
                Galley.append('')
            try:
                Refrigeration.append(boat.find(class_="row Boat_Field_Row Boat_Refrigeration").find_all('div')[-1].text)
            except:
                Refrigeration.append('')
            try:
                Freezer.append(boat.find(class_="row Boat_Field_Row Boat_Freezer").find_all('div')[-1].text)
            except:
                Freezer.append('')
            try:
                Water_Maker.append(boat.find(class_="row Boat_Field_Row Boat_WaterMaker").find_all('div')[-1].text)
            except:
                Water_Maker.append('')
            try:
                Mast_Rigging.append(boat.find(class_="row Boat_Field_Row Boat_Rigging").find_all('div')[-1].text)
            except:
                Mast_Rigging.append('')
            try:
                Stove.append(boat.find(class_="row Boat_Field_Row Boat_Stove").find_all('div')[-1].text.strip())
            except:
                Stove.append('')
            try:
                Hot_Water.append(boat.find(class_="row Boat_Field_Row Boat_HotWaterSystem").find_all('div')[-1].text)
            except:
                Hot_Water.append('')
            try:
                Safety_Gear.append(boat.find(class_="row Boat_Field_Row Boat_SafetyGear").find_all('div')[-1].text.strip())
            except:
                Safety_Gear.append('')
            try:
                Sail_Inventory.append(boat.find(class_="col-sm-2 Label Boat_SailInventory_Label").find_all('div')[-1].text.strip())
            except:
                Sail_Inventory.append('')
            try:
                Deck_Gear.append(boat.find(class_="row Boat_Field_Row Boat_DeckGear").find_all('div')[-1].text)
            except:
                Deck_Gear.append('')
            try:
                Bilge_Pumps.append(boat.find(class_="row Boat_Field_Row Boat_BilgePumps").find_all('div')[-1].text)
            except:
                Bilge_Pumps.append('')
            try:
                Fire_Protection.append(boat.find(class_="row Boat_Field_Row Boat_FireProtection").find_all('div')[-1].text)
            except:
                Fire_Protection.append('')
            try:
                Life_Raft.append(boat.find(class_="row Boat_Field_Row Boat_LifeRaft").find_all('div')[-1].text)
            except:
                Life_Raft.append('')
            try:
                Life_Jackets.append(boat.find(class_="row Boat_Field_Row Boat_LifeJackets").find_all('div')[-1].text)
            except:
                Life_Jackets.append('')
            try:
                Accommodation.append(boat.find(class_="row Boat_Field_Row Boat_Accommodation").find_all('div')[-1].text)
            except:
                Accommodation.append('')
            try:
                Air_Conditioning.append(boat.find(class_="row Boat_Field_Row Boat_AirConditioning").find_all('div')[-1].text)
            except:
                Air_Conditioning.append('')
            try:
                Electrics.append(boat.find(class_="row Boat_Field_Row Boat_Electrics").find_all('div')[-1].text)
            except:
                Electrics.append('')
            try:
                Electronics_Navigation.append(boat.find(class_="row Boat_Field_Row Boat_Electronics").find_all('div')[-1].text)
            except:
                Electronics_Navigation.append('')
            try:
                Broker_Dealer.append(boat.find(class_="row Boat_Field_Row User_Name").find_all('div')[-1].text.strip())
            except:
                Broker_Dealer.append('')
            try:
                Telephone.append(boat.find(class_="row Boat_Field_Row User_Phone js-clickme_phone").find(class_="hidden").text)
            except:
                Telephone.append('')
            try:
                Address.append(boat.find(class_="row Boat_Field_Row User_Address").find(class_="col-sm-8 Field").text.strip())
            except:
                Address.append('')
            try:
                City_Suburb.append(boat.find(class_="row Boat_Field_Row User_City").find(class_="col-sm-8 Field").text.strip())
            except:
                City_Suburb.append('')
            try:
                State.append(boat.find(class_="row Boat_Field_Row User_State").find(class_="col-sm-8 Field").text.strip())
            except:
                State.append('')
            try:
                Country.append(boat.find(class_="row Boat_Field_Row User_Country").find(class_="col-sm-8 Field").text.strip())
            except:
                Country.append('')
            try:
                Website.append(boat.find(class_="row Boat_Field_Row User_Website").find(class_="col-sm-8 Field").a['href'])
            except:
                Website.append('')
            try:
                Url.append(f_url)
            except:
                Url.append('')
        # check whether there are more listings for a brand in next pages
        try:
            next_page=bs.find_all(class_="icon-chevron-right")[0]['href']
            if next_page!='javascript:void(0)':
                if int(next_page[-1])==9:
                    raise ValueError('page number 9: {}'.format(make))
                url=r'https://www.boatsonline.com.au'+next_page
                req=requests.get(url)
                bs=BeautifulSoup(req.text,'html.parser')
                boats=bs.find_all(class_="article listing-container")
            else:
                boats=False
        except:
            boats=False

    #store properties in a dictionary 
    d=dict(Name=Name,
    Model=Model
    ,Make=Make
    ,Status=Status
    ,Price=Price
    ,Image=Image
    ,Length=Length
    ,Use=Use
    ,Location=Location
    ,Launch_Year=Launch_Year
    ,Hull=Hull
    ,Region=Region
    ,Displacement=Displacement
    ,Keel_Ballast=Keel_Ballast
    ,Decks_Material=Decks_Material
    ,Beam=Beam
    ,Draft=Draft
    ,Registration=Registration
    ,Rego_Expiry=Rego_Expiry
    ,Engine_Make=Engine_Make
    ,Engine=Engine
    ,Number_Engines=Number_Engines
    ,Horse_Power=Horse_Power
    ,Fuel_Type=Fuel_Type
    ,Engine_Hours=Engine_Hours
    ,Fuel_Consumption=Fuel_Consumption
    ,Propulsion=Propulsion
    ,Max_Speed=Max_Speed
    ,Cruise_Speed=Cruise_Speed
    ,Genset=Genset
    ,Fuel=Fuel
    ,Water=Water
    ,Dinghy=Dinghy
    ,Outboard=Outboard
    ,Covers=Covers
    ,Berths=Berths
    ,Shower=Shower
    ,Toilet=Toilet
    ,Entertainment=Entertainment
    ,Galley=Galley
    ,Refrigeration=Refrigeration
    ,Freezer=Freezer
    ,Water_Maker=Water_Maker
    ,Mast_Rigging=Mast_Rigging
    ,Stove=Stove
    ,Hot_Water=Hot_Water
    ,Safety_Gear=Safety_Gear
    ,Sail_Inventory=Sail_Inventory
    ,Deck_Gear=Deck_Gear
    ,Bilge_Pumps=Bilge_Pumps
    ,Fire_Protection=Fire_Protection
    ,Life_Raft=Life_Raft
    ,Life_Jackets=Life_Jackets
    ,Accommodation=Accommodation
    ,Air_Conditioning=Air_Conditioning
    ,Electrics=Electrics
    ,Electronics_Navigation=Electronics_Navigation
    ,Broker_Dealer=Broker_Dealer
    ,Telephone=Telephone
    ,Address=Address
    ,City_Suburb=City_Suburb
    ,State=State
    ,Country=Country
    ,Website=Website
    ,Url=Url)
    #make a dataframe from dictionary
    df=pd.DataFrame(d)
    df = df.applymap(lambda x: str(x).strip())
    #store listings of a brand in excel file
    with pd.ExcelWriter(r'{}.xlsx'.format(make['value'].replace('/','-').replace('\\','-'))) as writer:
        df.to_excel(writer,encoding='utf-8',engine='xlsxwriter')
    # continue the loop for next brand
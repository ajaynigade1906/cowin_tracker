from .call_api import CallApi

from datetime import datetime


url = "https://cdn-api.co-vin.in/api/v2"
availability_by_pin_code = f"{url}/appointment/sessions/public/calendarByPin"
availability_by_district = f"{url}/appointment/sessions/public/calendarByDistrict"
DD_MM_YYYY = "%d-%m-%Y"

district_name_with_id = {'north and middle andaman': '1', 'south andaman': '2', 'nicobar': '3', 'krishna': '4', 'guntur': '5', 'ysr district kadapa (cuddapah)': '6', 'kurnool': '7', 'visakhapatnam': '8', 'anantapur': '9', 'chittoor': '10', 'east godavari': '11', 'prakasam': '12', 'sri potti sriramulu nellore': '13', 'srikakulam': '14', 'vizianagaram': '15', 'west godavari': '16', 'itanagar capital complex': '17', 'pakke kessang': '19', 'changlang': '20', 'east kameng': '23', 'kamle': '24', 'dibang valley': '25', 'tirap': '26', 'kra daadi': '27', 'west kameng': '28', 'lohit': '29', 'tawang': '30', 'lower dibang valley': '31', 'lower subansiri': '32', 'lepa rada': '33', 'upper siang': '34', 'shi yomi': '35', 'namsai': '36', 'siang': '37', 'west siang': '38', 'papum pare': '39', 'longding': '40', 'upper subansiri': '41', 'east siang': '42', 'dibrugarh': '43', 'sivasagar': '44', 'tinsukia': '45', 'baksa': '46', 'barpeta': '47', 'darrang': '48', 'kamrup metropolitan': '49', 'kamrup rural': '50', 'karbi-anglong': '51', 'nalbari': '52', 'golaghat': '53', 'jorhat': '54', 'morigaon': '55', 'nagaon': '56', 'bongaigaon': '57', 'chirang': '58', 'dhubri': '59', 'goalpara': '60', 'kokrajhar': '61', 'dhemaji': '62', 'lakhimpur': '63', 'sonitpur': '64', 'udalguri': '65', 'cachar': '66', 'dima hasao': '67', 'hailakandi': '68', 'karimganj': '69', 'madhepura': '70', 'saharsa': '71', 'supaul': '72', 'purnia': '73', 'araria': '74', 'katihar': '75', 'kishanganj': '76', 'aurangabad': '77', 'gaya': '79', 'kaimur': '80', 'rohtas': '81', 'bhagalpur': '82', 'banka': '83', 'lakhisarai': '84', 'munger': '85', 'muzaffarpur': '86', 'sheohar': '87', 'sitamarhi': '88', 'vaishali': '89', 'nalanda': '90', 'jehanabad': '91', 'nawada': '92', 'sheikhpura': '93', 'darbhanga': '94', 'madhubani': '95', 'samastipur': '96', 'patna': '97', 'begusarai': '98', 'bhojpur': '99', 'buxar': '100', 'khagaria': '101', 'saran': '102', 'siwan': '103', 'gopalganj': '104', 'east champaran': '105', 'west champaran': '106', 'jamui': '107', 'chandigarh': '108', 'raipur': '109', 'balod': '110', 'baloda bazar': '111', 'balrampur': '112', 'bastar': '113', 'bemetara': '114', 'bijapur': '115', 'bilaspur': '116', 'dantewada': '117', 'dhamtari': '118', 'durg': '119', 'gariaband': '120', 'janjgir-champa': '121', 'jashpur': '122', 'kanker': '123', 'kondagaon': '124', 'korba': '125', 'koriya': '126', 'mahasamund': '127', 'mungeli': '128', 'narayanpur': '129', 'raigarh': '130', 'rajnandgaon': '131', 'sukma': '132', 'surajpur': '133', 'surguja': '134', 'kawardha': '135', 'gaurela pendra marwahi ': '136', 'dadra and nagar haveli': '137', 'daman': '138', 'diu': '139', 'new delhi': '140', 'central delhi': '141', 'west delhi': '142', 'north west delhi': '143', 'south east delhi': '144', 'east delhi': '145', 'north delhi': '146', 'north east delhi': '147', 'shahdara': '148', 'south delhi': '149', 'south west delhi': '150', 'north goa': '151', 'south goa': '152', 'gandhinagar': '153', 'ahmedabad': '154', 'vadodara': '155', 'kheda': '156', 'surendranagar': '157', 'aravalli': '158', 'banaskantha': '159', 'mehsana': '160', 'patan': '161', 'sabarkantha': '162', 'dang': '163', 'navsari': '164', 'surat': '165', 'tapi': '166', 'valsad': '167', 'devbhumi dwaraka': '168', 'jamnagar': '169', 'kutch': '170', 'morbi': '171', 'porbandar': '172', 'rajkot': '173', 'amreli': '174', 'bhavnagar': '175', 'botad': '176', 'gir somnath': '177', 'junagadh': '178', 'anand': '179', 'bharuch': '180', 'chhotaudepur': '181', 'dahod': '182', 'mahisagar': '183', 'narmada': '184', 'panchmahal': '185', 'kurukshetra': '186', 'panchkula': '187', 'gurgaon': '188', 'jhajjar': '189', 'kaithal': '190', 'hisar': '191', 'rohtak': '192', 'ambala': '193', 'sirsa': '194', 'panipat': '195', 'fatehabad': '196', 'yamunanagar': '197', 'sonipat': '198',
'faridabad': '199', 'bhiwani': '200', 'charkhi dadri': '201', 'rewari': '202', 'karnal': '203', 'jind': '204', 'nuh': '205', 'mahendragarh': '206', 'palwal': '207', 'shimla': '208', 'solan': '209', 'lahaul spiti': '210', 'kullu': '211', 'sirmaur': '212', 'kangra': '213', 'chamba': '214', 'mandi': '215', 'kinnaur': '216', 'hamirpur': '217', 'una': '218', 'bilaspur': '219', 'srinagar': '220', 'kulgam': '221', 'shopian': '222', 'bandipore': '223', 'anantnag': '224', 'baramulla': '225', 'kupwara': '226', 'ganderbal': '228', 'budgam': '229', 'jammu': '230', 'kishtwar': '231', 'doda': '232', 'udhampur': '233', 'kathua': '234', 'ramban': '235', 'samba': '236', 'rajouri': '237', 'poonch': '238', 'reasi': '239', 'ranchi': '240', 'koderma': '241', 'bokaro': '242', 'garhwa': '243', 'latehar': '244', 'chatra': '245', 'palamu': '246', 'east singhbhum': '247', 'seraikela kharsawan': '248', 'simdega': '249', 'lohardaga': '250', 'gumla': '251', 'khunti': '252', 'deoghar': '253', 'ramgarh': '254', 'hazaribagh': '255', 'giridih': '256', 'dhanbad': '257', 'dumka': '258', 'jamtara': '259', 'sahebganj': '260', 'pakur': '261', 'godda': '262', 'west singhbhum': '263', 'belgaum': '264', 'bangalore urban': '265', 'mysore': '266', 'gulbarga': '267', 'chitradurga': '268', 'dakshina kannada': '269', 'bagalkot': '270', 'chamarajanagar': '271', 'bidar': '272', 'chikamagalur': '273', 'bellary': '274', 'davanagere': '275', 'bangalore rural': '276', 'kolar': '277', 'dharwad': '278', 'haveri': '279', 'gadag': '280', 'uttar kannada': '281', 'koppal': '282', 'kodagu': '283', 'raichur': '284', 'yadgir': '285', 'udupi': '286', 'shimoga': '287', 'hassan': '289', 'mandya': '290', 'chikkaballapur': '291', 'ramanagara': '292', 'vijayapura': '293', 'bbmp': '294', 'kasaragod': '295', 'thiruvananthapuram': '296', 'kannur': '297', 'wayanad': '299', 'pathanamthitta': '300', 'alappuzha': '301', 'malappuram': '302', 'thrissur': '303', 'kottayam': '304', 'kozhikode': '305', 'idukki': '306', 'ernakulam': '307', 'palakkad': '308', 'kargil': '309', 'leh': '310', 'lakshadweep': '311', 'bhopal': '312', 'gwalior': '313', 'indore': '314', 'jabalpur': '315', 'rewa': '316', 'sagar': '317', 'ujjain': '318', 'mandsaur': '319', 'agar': '320', 'shajapur': '321', 'ratlam': '322', 'neemuch': '323', 'dewas': '324', 'tikamgarh': '325', 'panna': '326', 'damoh': '327', 'chhatarpur': '328', 'umaria': '329', 'singrauli': '330', 'sidhi': '331', 'shahdol': '332', 'satna': '333', 'anuppur': '334', 'mandla': '335', 'dindori': '336', 'chhindwara': '337', 'balaghat': '338', 'khandwa': '339', 'jhabua': '340', 'dhar': '341', 'burhanpur': '342', 'barwani': '343', 'khargone': '344', 'shivpuri': '345', 'sheopur': '346', 'morena': '347', 'guna': '348', 'seoni': '349', 'datia': '350', 'bhind': '351', 'narsinghpur': '352', 'katni': '353', 'ashoknagar': '354', 'vidisha': '355', 'sehore': '356', 'alirajpur': '357', 'rajgarh': '358', 'raisen': '359', 'hoshangabad': '360', 'harda': '361', 'betul': '362', 'pune': '363', 'akola': '364', 'nagpur': '365', 'amravati': '366', 'buldhana': '367', 'yavatmal': '368', 'washim': '369', 'bhandara': '370', 'kolhapur': '371', 'ratnagiri': '372', 'sangli': '373', 'sindhudurg': '374', 'solapur': '375', 'satara': '376', 'wardha': '377', 'gondia': '378', 'gadchiroli': '379', 'chandrapur': '380', 'osmanabad': '381', 'nanded': '382', 'latur': '383', 'beed': '384', 'parbhani': '385', 'hingoli': '386', 'nandurbar': '387', 'dhule': '388', 'nashik': '389', 'jalgaon': '390', 'ahmednagar': '391', 'thane': '392', 'raigad': '393', 'palghar': '394', 'jalna': '396', 'aurangabad ': '397', 'bishnupur': '398', 'chandel': '399', 'churachandpur': '400', 'imphal east': '401', 'imphal west': '402', 'tamenglong': '404', 'thoubal': '405', 'tengnoupal': '407', 'kamjong': '409',
'jiribam': '410', 'pherzawl': '411', 'noney': '412', 'kakching': '413', 'east khasi hills': '414', 'south west khasi hills': '415', 'west jaintia hills': '416', 'ri-bhoi': '417', 'east jaintia hills': '418', 'west khasi hills': '419', 'west garo hills': '420', 'south garo hills': '421', 'south west garo hills': '422', 'north garo hills': '423', 'east garo hills': '424', 'aizawl east': '425', 'aizawl west': '426', 'mamit': '427', 'kolasib': '428', 'champhai': '429', 'serchhip': '430', 'lunglei': '431', 'lawngtlai': '432', 'siaha': '433', 'dimapur': '434', 'peren': '435', 'wokha': '436', 'mokokchung': '437', 'longleng': '438', 'mon': '439', 'tuensang': '440', 'kohima': '441', 'zunheboto': '442', 'phek': '443', 'kiphire': '444', 'angul': '445', 'khurda': '446', 'balasore': '447', 'balangir': '448', 'ganjam': '449', 'kandhamal': '450', 'koraput': '451', 'sambalpur': '452', 'sundargarh': '453', 'bhadrak': '454', 'kendujhar': '455', 'mayurbhanj': '456', 'cuttack': '457', 'dhenkanal': '458', 'jajpur': '460', 'kendrapara': '461', 'nayagarh': '462', 'puri': '463', 'kalahandi': '464', 'nuapada': '465', 'subarnapur': '466', 'gajapati': '467', 'boudh': '468', 'malkangiri': '469', 'nabarangpur': '470', 'rayagada': '471', 'bargarh': '472', 'deogarh': '473', 'jharsuguda': '474', 'puducherry': '475', 'karaikal': '476', 'yanam': '478', 'kapurthala': '479', 'ferozpur': '480', 'hoshiarpur': '481', 'mansa': '482', 'barnala': '483', 'fatehgarh sahib': '484', 'amritsar': '485', 'pathankot': '486', 'fazilka': '487', 'ludhiana': '488', 'gurdaspur': '489', 'sri muktsar sahib': '490', 'moga': '491', 'jalandhar': '492', 'bathinda': '493', 'patiala': '494', 'tarn taran': '495', 'sas nagar': '496', 'rup nagar': '497', 'sangrur': '498', 'faridkot': '499', 'sbs nagar': '500', 'bikaner': '501', 'jodhpur': '502', 'kota': '503', 'udaipur': '504', 'jaipur i': '505', 'jaipur ii': '506', 'ajmer': '507', 'bharatpur': '508', 'sri ganganagar': '509', 'jhunjhunu': '510', 'dausa': '511', 'alwar': '512', 'sikar': '513', 'bundi': '514', 'jhalawar': '515', 'baran': '516', 'hanumangarh': '517', 'rajsamand': '518', 'banswara': '519', 'dungarpur': '520', 'chittorgarh': '521', 'pratapgarh': '522', 'bhilwara': '523', 'dholpur': '524', 'karauli': '525', 'tonk': '526', 'jaisalmer': '527', 'barmer': '528', 'pali': '529', 'churu': '530', 'sirohi': '531', 'nagaur': '532', 'jalore': '533', 'sawai madhopur': '534', 'east sikkim': '535', 'west sikkim': '536', 'north sikkim': '537', 'south sikkim': '538', 'coimbatore': '539', 'madurai': '540', 'thanjavur': '541', 'viluppuram': '542', 'vellore': '543', 'kanyakumari': '544', 'salem': '545', 'pudukkottai': '546', 'cuddalore': '547', 'tirunelveli': '548', 'virudhunagar': '549', 'tirupattur': '550', 'tenkasi': '551', 'kallakurichi': '552', 'tiruvannamalai': '553', 'thoothukudi (tuticorin)': '554', 'ariyalur': '555', 'dindigul': '556', 'kanchipuram': '557', 'namakkal': '558', 'karur': '559', 'tiruchirappalli': '560', 'sivaganga': '561', 'krishnagiri': '562', 'erode': '563', 'palani': '564', 'chengalpet': '565', 'dharmapuri': '566', 'ramanathapuram': '567', 'tiruppur': '568', 'theni': '569', 'perambalur': '570', 'chennai': '571', 'tiruvallur': '572', 'paramakudi': '573', 'tiruvarur': '574', 'poonamallee': '575', 'nagapattinam': '576', 'nilgiris': '577', 'attur': '578', 'sivakasi': '580', 'hyderabad': '581', 'adilabad': '582', 'bhadradri kothagudem': '583', 'jagtial': '584', 'jangaon': '585', 'jayashankar bhupalpally': '586', 'jogulamba gadwal': '587', 'kamareddy': '588', 'karimnagar': '589', 'khammam': '590', 'kumuram bheem': '591', 'mahabubabad': '592', 'mahabubnagar': '593', 'mancherial': '594', 'medak': '595', 'medchal': '596', 'nagarkurnool': '597', 'nalgonda': '598', 'nirmal': '599', 'nizamabad': '600', 'peddapalli': '601', 'rajanna sircilla': '602', 'rangareddy': '603', 'sangareddy': '604', 'siddipet': '605', 'suryapet': '606', 'vikarabad': '607', 'wanaparthy': '608', 'warangal(rural)': '609', 'warangal(urban)': '610', 'yadadri bhuvanagiri': '611', 'mulugu': '612', 'narayanpet': '613', 'dhalai': '614', 'gomati': '615', 'khowai': '616', 'north tripura': '617', 'sepahijala': '618', 'south tripura': '619', 'unakoti': '620', 'west tripura': '621', 'agra': '622', 'aligarh': '623', 'prayagraj': '624', 'ambedkar nagar': '625', 'amethi': '626', 'amroha': '627', 'auraiya': '628', 'azamgarh': '629', 'badaun': '630', 'baghpat': '631', 'bahraich': '632', 'balarampur': '633', 'ballia': '634', 'banda': '635', 'barabanki': '636', 'bareilly': '637', 'basti': '638', 'bijnour': '639', 'bulandshahr': '640', 'chandauli': '641', 'chitrakoot': '642', 'deoria': '643', 'etah': '644', 'ayodhya': '646', 'fatehpur': '648', 'ghaziabad': '651', 'hamirpur': '655', 'jalaun': '659',
'jaunpur': '660', 'jhansi': '661', 'kannauj': '662', 'kanpur dehat': '663', 'kanpur nagar': '664', 'kasganj': '665', 'kaushambi': '666', 'kushinagar': '667', 'lakhimpur kheri': '668', 'lalitpur': '669', 'lucknow': '670', 'maharajganj': '671', 'mahoba': '672', 'mainpuri': '673', 'mathura': '674', 'mau': '675', 'meerut': '676', 'mirzapur': '677', 'moradabad': '678', 'muzaffarnagar': '679', 'pilibhit': '680', 'raebareli': '681', 'pratapgarh': '682', 'rampur': '683', 'saharanpur': '684', 'sambhal': '685', 'sant kabir nagar': '686', 'bhadohi': '687', 'shahjahanpur': '688', 'shamli': '689', 'shravasti': '690', 'siddharthnagar': '691', 'sitapur': '692', 'sonbhadra': '693', 'sultanpur': '694', 'unnao': '695', 'varanasi': '696', 'dehradun': '697', 'pauri garhwal': '698', 'chamoli': '699', 'rudraprayag': '700', 'tehri garhwal': '701', 'haridwar': '702', 'uttarkashi': '703', 'almora': '704', 'udham singh nagar': '705', 'pithoragarh': '706', 'bageshwar': '707', 'champawat': '708', 'nainital': '709', 'alipurduar district': '710', 'bankura': '711', 'basirhat hd (north 24 parganas)': '712', 'birbhum': '713', 'bishnupur hd (bankura)': '714', 'dakshin dinajpur': '716', 'darjeeling': '717', 'diamond harbor hd (s 24 parganas)': '718', 'east bardhaman': '719', 'hoogly': '720', 'howrah': '721', 'jalpaiguri': '722', 'jhargram': '723', 'kalimpong': '724', 'kolkata': '725', 'malda': '726', 'murshidabad': '727', 'nadia': '728', 'nandigram hd (east medinipore)': '729', 'north 24 parganas': '730', 'paschim medinipore': '731', 'purba medinipore': '732', 'purulia': '733', 'rampurhat hd (birbhum)': '734', 'south 24 parganas': '735', 'uttar dinajpur': '736', 'west bardhaman': '737'}

class Parser(CallApi):
    def get_availability(self, caller,
                                 area_id,
                                 date: str, min_age_limt: int):
        try:
            area_type, url = 'pincode', availability_by_pin_code
            if caller == 'district':
                area_type, url = 'district_id', availability_by_district
            # if the areas is a str, convert to list
            #if isinstance(areas, str):
            #    areas = [areas]
            # make a separate call for each of the areas
            results = []
            #for area_id in areas:
            url = f"{url}?{area_type}={area_id}&date={date}"
            if min_age_limt:
                curr_result = filter_centers_by_age_limit(self._api_call(url),
                                                          min_age_limt)
            else:
                curr_result = self._api_call(url)
            # append
            if curr_result:
                results += curr_result['centers']
            return {'centers': results}
        except:
            print('URL responce code is'+ str(curr_result.status_code))
        
    def get_availability_by_name(self, caller,
                                 area_name,
                                 date: str, min_age_limt: int):
        try:
            if caller == 'district':
                area_type, url = 'district_id', availability_by_district
            # if the areas is a str, convert to list
            #if isinstance(areas, str):
            #    areas = [areas]
            # make a separate call for each of the areas
            results = []
            #for area_id in areas:
            try :
                area_id = district_name_with_id[area_name]
            except KeyError:
                print(f"{area_name}'s district is unknown, please enter correct district name")
            url = f"{url}?{area_type}={area_id}&date={date}"
            if min_age_limt:
                curr_result = filter_centers_by_age_limit(self._api_call(url),
                                                          min_age_limt)
            else:
                curr_result = self._api_call(url)
            # append
            if curr_result:
                results += curr_result['centers']
            return {'centers': results}
        except:
            #import pdb;pdb.set_trace()
            if 'curr_result' in locals() :
                print('URL responce code is'+ str(curr_result.status_code))

    def today() -> str:
        return datetime.now().strftime(DD_MM_YYYY)

def filter_centers_by_age_limit(centers: dict, min_age_limit: int):
    original_center = centers.get('centers')
    filtered_center = {'centers': []}
    for index, center in enumerate(original_center):
        filtered_session = []
        for session in center.get('sessions'):
            if session.get('min_age_limit') == min_age_limit:
                filtered_session.append(session)
        if len(filtered_session) > 0:
            center['sessions'] = filtered_session
            filtered_center['centers'].append(center)

    return filtered_center
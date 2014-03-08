# -*- coding: utf-8 -*-
""" Property Constants
	@author Lionel Cuevas <lionel@hoopemedia.com>"""

CATEGORIES = {
    1:'Departamentos',
    2:'Casas',
    3:'PH',
    4:'Countries y barrios cerrados',
    5:'Quintas',
    6:'Terrenos y lotes',
    7:'Campos y chacras',
    8:'Galpones, depósitos y edificios industriales',
    9:'Locales comerciales',    
    10:'Oficinas',
    11:'Consultorios',
    12:'Cocheras',
}
SUBCATEGORIES = {
    1:{1:'Dúplex', 2:'Triplex', 3:'Loft', 4:'Piso', 5:'Semipiso', 6:'Penthouse', 7:'Departamento'},
    2:{8:'Dúplex', 9:'Triplex', 10:'Chalet', 11:'Cabaña', 12:'Casa'},
    3:{13:'PH'},
    4:{14:'Casa',15:'Departamento',16:'Terreno'},
    5:{17:'Quintas'},
    6:{18:'Terrenos y lotes'},
    7:{19:'Campos y chacras'},
    8:{20:'Galpones', 21:'Depósitos', 22:'Edificios industriales'},
    9:{23:'Locales comerciales'},    
    10:{24:'Oficinas'},
    11:{25:'Consultorios'},
    12:{26:'Cocheras'},
}
OPERATION_TYPE = {
    1: 'Venta',
    2: 'Alquiler',
    3: 'Emprendimiento'
}
PROPERTYFORM = {
    1:{1:'Department', 2:'Department', 3:'Department', 4:'Department', 5:'Department', 6:'Department', 7:'Department'},
    2:{8:'House', 9:'House', 10:'House', 11:'House', 12:'House'},
    3:{13:'PH'},
    4:{14:'House',15:'Department',16:'Land'},
    5:{17:'CountryHouse'},
    6:{18:'Land'},
    7:{19:'Field'},
    8:{20:'Shed', 21:'Storage', 22:'IndustrialBuilding'},
    9:{23:'Local'},    
    10:{24:'Office'},
    11:{25:'ConsultingRoom'},
    12:{26:'Garage'},
}   
DISPOSITION_TYPE = {
    0:'No especificado',
    1:'Frente',
    2:'Contrafrente',
    3:'Interno',
    4:'Lateral',
}
UNITY_TYPE = {
    0:'No especificado',
    1:'Loft',
    2:'Departamento',
    3:'Semipiso',
    4:'Piso',
    5:'Duplex',
    6:'Penthouse',
}
QUANTITY = {
    0:'No especificado',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5 o más'       
}
ORIENTATION_TYPE = {
    0:'No especificado',
    1:'N',
    2:'S',
    3:'E',
    4:'O',
    5:'NE',
    6:'NO',
    7:'SE',
    8:'SO',
}
BUILDING_TYPE = {
    0:'No especificado',
    1:'Entre medianeras',
    2:'Torre',
    3:'Tipo Block',
    4:'Esquina',
    5:'Antiguo',
    6:'Inteligente',
    7:'Primera Categoria',
    8:'Estándar',
}
BUILDING_STATUS = {
    0:'No especificado',
    1:'Reciclado',
    2:'Excelente',
    3:'Muy Bueno',
    4:'Bueno',
    5:'Regular',
    6:'A Refaccionar'  
}
BUILDING_CATEGORY = {
    0:'No especificado',
    1:'Excelente',
    2:'Muy Buena',
    3:'Buena',
    4:'Estándar',
    5:'Económica'    
}
SUITABLE = {
    0:'No especificado',
    1:'Si',
    2:'No'
}
LIGHTNESS = {
    0:'No especificado',
    1:'Muy luminoso',
    2:'Luminoso',
    3:'Poco luminoso',
}
ROOF_TYPE = {
    0:'No especificado',
    1:'Chapa',
    2:'Losa',
    3:'Pizzarra',
    4:'Teja',
}
GATE_TYPE = {
    0:'No especificado',
    1:'Corredizo',
    2:'Levadizo',        
}
INDUSTRIAL_ROOF_TYPE = {
    0:'No especificado',
    1:'Astori',
    2:'Bobedilla',
    3:'Cabriada',
    4:'Chapa',
    5:'Dos aguas',
    6:'Fibrocemento',
    7:'Galvanizado',
    8:'Hormigón',
    9:'Losa',
    10:'Parabolico',
    11:'Premoldeado',
    12:'Tinglado',
    14:'Tres aguas',
    15:'Zinc',
    16:'Otro',
}
FIELDS_LABELS = {
    'creation_date':'Creado',
    'antiqueness':'Antiguedad',
    'square_meters':'Metros Cuadrados (m2)',
    'total_meters':'Superficie total (m2)',
    'total_uncovered_meters':'Superficie descubierta (m2)',
    'suitableProfessional': 'Apto profesional',
    'suitableCredit':'Apto Crédito',
    'providesFunding':'Ofrece Financiación',
    'commercialUsage':'Apto profesional',
    'quantityAmbiences': 'Cantidad de ambientes',
    'quantityBedrooms': 'Cantidad de dormitorios',  
    'quantityBathrooms':'Cantidad de baños',
    'quantityGarages':'Cantidad de cocheras',
    'garageCoverage':'Cobertura cochera',
    'orientation':'Orientación',
    'disposition':'Disposición',
    'buildingType':'Tipo de Edificio',
    'buildingCondition': 'Estado del Inmueble',
    'buildingStatus': 'Estado del Edificio',
    'buildingCategory': 'Categoría del Edificio',
    'apartmentsPerFloor': 'Departamentos por piso',
    'quantityBuildingFloors': 'Cantidad de pisos en edificio',    
    'floorNumber': 'Piso',
    'quantityElevators': 'Cantidad de Ascensores',
    'expenses': 'Expensas ($)',
    'lightness': 'Luminosidad',
    'roofType': 'Tipo de techo',
    'frontGround': 'Frente del terreno (mts)',
    'largeGround': 'Largo del terreno (mts)',
    'hectares': 'Hectáreas',
    'fot': 'F.O.T.',
    'industrialRoofType': 'Tipo de techo industrial',
    'roofHeight': 'Altura del techo',
    'gateType': 'Tipo de portón',
    'quantityShips': 'Cantidad de naves',
    'unityType': 'Tipo de unidad',
    'quantityFloors': 'Cantidad de plantas',
}
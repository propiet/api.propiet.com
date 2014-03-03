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
    8:'Galpones:depósitos y Edificios',
    9:'Locales comerciales',
    10:'Negocios y Fondos de Comercio',
    11:'Oficinas',
    12:'Consultorios',
    13:'Cocheras',
}
SUBCATEGORIES = {
    1:{1:'Dúplex', 2:'Triplex', 3:'Loft', 4:'Piso', 5:'Semipiso', 6:'Penthouse', 7:'Departamento'},
    2:{1:'Dúplex', 2:'Triplex', 3:'chalet', 4:'Cabaña', 5:'Casa'},
    3:{1:'PH'},
    4:{1:'Casa',2:'Departamento',3:'Terreno'},
    5:{1:'Quintas'},
    6:{1:'Terrenos y lotes'},
    7:{1:'Campos y chacras'},
    8:{1:'Galpones', 2:'Depósitos', 3:'Edificios Industriales'},
    9:{1:'Locales comerciales'},
    10:{1:'Negocios y Fondos de Comercio'},
    11:{1:'Oficinas'},
    12:{1:'Consultorios'},
    13:{1:'Cocheras'},
}
OPERATION_TYPE = {
    1: 'Venta',
    2: 'Alquiler'
}
PROPERTYFORM = {
    1:{1:'Department', 2:'Department', 3:'Department', 4:'Department', 5:'Department', 6:'Department', 7:'Department'},
    2:{1:'House', 2:'House', 3:'House', 4:'House', 5:'House'},
    3:{1:'PH'},
    4:{1:'House',2:'Department',3:'Land'},
    5:{1:'CountryHouse'},
    6:{1:'Land'},
    7:{1:'Field'},
    8:{1:'Shed', 2:'Storage', 3:'IndustrialBuilding'},
    9:{1:'Local'},
    10:{1:'Goodwill'},
    11:{1:'Office'},
    12:{1:'ConsultingRoom'},
    13:{1:'Garage'},
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
FIELD_LABEL = {
    'creation_date':'Creado',
    'antiqueness':'Antiguedad',
    'square_meters':'Mt2',
    'total_meters':'Mts Totales',
    'total_uncovered_meters':'Metros descubiertos',
    'suitableProfessional': 'Apto profesional',
    'suitableCredit':'Apto Crédito',
    'providesFunding':'Ofrece Financiación',
    'quantityBedrooms': 'Cantidad de Dormitorios',  
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
    'quantityBuildingFloors': 'Cantidad de pisos en edificio',
    'floorNumber': 'Piso',
    'quantityElevators': 'Cantidad de Ascensores',
    'expenses': 'Expensas',
    'lightness': 'Luminosidad',
    'roofType': 'Tipo techo',
    'frontGround': 'Metros de Frente',
    'largeGround': 'Metros de Largo',
    'hectares': 'Hectáreas',
    'fot': 'FOT'

}
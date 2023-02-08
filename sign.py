import time
from select import select
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver")
driver.maximize_window()
driver.implicitly_wait(5)

l = 0
mylist = [

    # 'https://signaling.fedsig.com/product/121aled',
    # 'https://signaling.fedsig.com/product/slm300-slm350-streamline',
    # 'https://signaling.fedsig.com/product/explosion-proof-industrial-telephone',
    # 'https://signaling.fedsig.com/product/break-glass-call-point',
    # 'https://signaling.fedsig.com/product/310-mv-audiomaster-two-way-intercom',
    # 'https://signaling.fedsig.com/product/310-mv-mnc-audiomaster-two-way-intercom',
    # 'https://signaling.fedsig.com/product/fire-alarm-pull-station',
    # 'https://signaling.fedsig.com/product/121aled-n-nsf',
    # 'https://signaling.fedsig.com/product/telb-telcom-telephone-extension-ringer-device',
    # 'https://signaling.fedsig.com/product/telc-telcom-telephone-extension-ringer-device',
    # 'https://signaling.fedsig.com/product/ps-series-push-button-station',
    # 'https://signaling.fedsig.com/product/121sled-n-nsf-certified-series-sanitation-rotating-led-warning-light',
    # 'https://signaling.fedsig.com/product/310x-mv-audiomaster-hazardous-location-two-way-intercom',
    # 'https://signaling.fedsig.com/product/ad-26-atkinson-dynamics-intercom',
    # 'https://signaling.fedsig.com/product/121sled-vitalite-rotating-led-warning-light',
    # 'https://signaling.fedsig.com/product/push-button-call-point',
    # 'https://signaling.fedsig.com/product/telh-telcom-telephone-extension-ringer-device',
    # 'https://signaling.fedsig.com/product/121x-explosion-proof-rotating-light',
    # 'https://signaling.fedsig.com/product/ad-26p-atkinson-dynamics-panel-mount-intercom',
    # 'https://signaling.fedsig.com/product/K122283A',
    # 'https://signaling.fedsig.com/product/K122341A',
    # 'https://signaling.fedsig.com/product/300fp-field-programmer',
    # 'https://signaling.fedsig.com/product/ad-27-atkinson-dynamics-intercom',
    # 'https://signaling.fedsig.com/product/131st-131dst-starfire-strobe-warning-light',
    # 'https://signaling.fedsig.com/product/K122342A',
    # 'https://signaling.fedsig.com/product/141st-electraflash-strobe-warning-light',
    # 'https://signaling.fedsig.com/product/300gc-selectone',
    # 'https://signaling.fedsig.com/product/ad-27p-atkinson-dynamics-panel-mount-intercom',
    # 'https://signaling.fedsig.com/product/ad-28x-mv-atkinson-dynamics-hazardous-location-intercom',
    # 'https://signaling.fedsig.com/product/151xst-hazardous-location-warning-light',
    # 'https://signaling.fedsig.com/product/300gcx-cn-selectone',
    # 'https://signaling.fedsig.com/product/K122348A',
    # 'https://signaling.fedsig.com/product/K122351A',
    # 'https://signaling.fedsig.com/product/300gcx-selectone',
    # 'https://signaling.fedsig.com/product/ad-56-atkinson-dynamics-intercom',
    # 'https://signaling.fedsig.com/product/154xsthi-and-154xst-cn',
    # 'https://signaling.fedsig.com/product/ad-56p-atkinson-dynamics-panel-mount-intercom',
    # 'https://signaling.fedsig.com/product/154xst-supervised-light',
    # 'https://signaling.fedsig.com/product/K122A299A',
    # 'https://signaling.fedsig.com/product/300mb-commcenter',
    # 'https://signaling.fedsig.com/product/KGL4076215',
    # 'https://signaling.fedsig.com/product/300scw-1-command-unit',
    # 'https://signaling.fedsig.com/product/191xl-cn',
    # 'https://signaling.fedsig.com/product/ad-57-atkinson-dynamics-intercom',
    # 'https://signaling.fedsig.com/product/ad-fp-foot-pedal',
    # 'https://signaling.fedsig.com/product/191xl-led',
    # 'https://signaling.fedsig.com/product/300-selectone-speaker',
    # 'https://signaling.fedsig.com/product/300vsc-1044sb-selectone-rack-mount-command-unit',
    # 'https://signaling.fedsig.com/product/adncm-noise-cancelling-microphone',
    # 'https://signaling.fedsig.com/product/300vsc-1-command-unit',
    # 'https://signaling.fedsig.com/product/K141A129A',
    # 'https://signaling.fedsig.com/product/225XST-n-nsf',
    # 'https://signaling.fedsig.com/product/304x-314x',
    # 'https://signaling.fedsig.com/product/31x-and-41x-horn',
    # 'https://signaling.fedsig.com/product/225xst-strobe',
    # 'https://signaling.fedsig.com/product/K143133A',
    # 'https://signaling.fedsig.com/product/350tr-vibratone-horn',
    # 'https://signaling.fedsig.com/product/K1461138A',
    # 'https://signaling.fedsig.com/product/24xst',
    # 'https://signaling.fedsig.com/product/24xsthi-supervised',
    # 'https://signaling.fedsig.com/product/K1461181A',
    # 'https://signaling.fedsig.com/product/350-vibratone-horn',
    # 'https://signaling.fedsig.com/product/K2001878B',
    # 'https://signaling.fedsig.com/product/27XHSNG',
    # 'https://signaling.fedsig.com/product/350wb-vibratone-horn',
    # 'https://signaling.fedsig.com/product/K2001878B-01',
    # 'https://signaling.fedsig.com/product/350wbx-vibratone-hazardous-location-horn',
    # 'https://signaling.fedsig.com/product/27xl-led-warning-light',
    # 'https://signaling.fedsig.com/product/K2001878B-02',
    # 'https://signaling.fedsig.com/product/27xst-4-supervised',
    # 'https://signaling.fedsig.com/product/3h-6h',
    # 'https://signaling.fedsig.com/product/450e-horn',
    # 'https://signaling.fedsig.com/product/K2001878B-02P',
    # 'https://signaling.fedsig.com/product/27xst-strobe-light',
    # 'https://signaling.fedsig.com/product/K2001878B-05',
    # 'https://signaling.fedsig.com/product/371BRCKT',
    # 'https://signaling.fedsig.com/product/450ewbx',
    # 'https://signaling.fedsig.com/product/K2001878B-07',
    # 'https://signaling.fedsig.com/product/TR',
    # 'https://signaling.fedsig.com/product/371dst-commander',
    # 'https://signaling.fedsig.com/product/504wb-506wb',
    # 'https://signaling.fedsig.com/product/371led-commander',
    # 'https://signaling.fedsig.com/product/K2001878B-08',
    # 'https://signaling.fedsig.com/product/50gcb-selectone',
    # 'https://signaling.fedsig.com/product/K2001878B-18',
    # 'https://signaling.fedsig.com/product/371ledx',
    # 'https://signaling.fedsig.com/product/50gc-selectone',
    # 'https://signaling.fedsig.com/product/av1-led',
    # 'https://signaling.fedsig.com/product/K2001878B-21',
    # 'https://signaling.fedsig.com/product/52-resonating-horn',
    # 'https://signaling.fedsig.com/product/av1st',
    # 'https://signaling.fedsig.com/product/55-and-56-resonating-horns',
    # 'https://signaling.fedsig.com/product/K2001896B',
    # 'https://signaling.fedsig.com/product/bpl26l-battery-powered',
    # 'https://signaling.fedsig.com/product/am15-audiomaster',
    # 'https://signaling.fedsig.com/product/K2001915C',
    # 'https://signaling.fedsig.com/product/blue-forklift-light-COMFL1-B-IS',
    # 'https://signaling.fedsig.com/product/am15xd2-audiomaster',
    # 'https://signaling.fedsig.com/product/K2001915C-02',
    # 'https://signaling.fedsig.com/product/ar2000-audiorouter',
    # 'https://signaling.fedsig.com/product/lp1-low-profile-strobe',
    # 'https://signaling.fedsig.com/product/ms-series-sounders-loudspeakers',
    # 'https://signaling.fedsig.com/product/lp22led-rgb-streamline',
    # 'https://signaling.fedsig.com/product/K8590289A',
    # 'https://signaling.fedsig.com/product/esiren',
    # 'https://signaling.fedsig.com/product/lp22led-streamline',
    # 'https://signaling.fedsig.com/product/es-series-sounders-loudspeakers',
    # 'https://signaling.fedsig.com/product/lp3-led',
    # 'https://signaling.fedsig.com/product/fhex-explosion-proof-vibrating-horn',
    # 'https://signaling.fedsig.com/product/sst3gcx-mv-hazardous-location-remotely-selectable-electronic-siren',
    # 'https://signaling.fedsig.com/product/lp3-strobe',
    # 'https://signaling.fedsig.com/product/lp6-mini-strobe',
    # 'https://signaling.fedsig.com/product/lp3g',
    # 'https://signaling.fedsig.com/product/sst3-mv-remotely-selectable-electronic-siren',
    # 'https://signaling.fedsig.com/product/sstx3-mv-explosion-proof-remotely-selectable-electronic-siren',
    # 'https://signaling.fedsig.com/product/lp7',
    # 'https://signaling.fedsig.com/product/tm33-selectone-custom-tone-module',
    # 'https://signaling.fedsig.com/product/lsl-litestak',
    # 'https://signaling.fedsig.com/product/LP57-mini-led',
    # 'https://signaling.fedsig.com/product/utm-selectone-universal-tone-module',
    # 'https://signaling.fedsig.com/product/msl-microstat',
    # 'https://signaling.fedsig.com/product/pmc',
    # 'https://signaling.fedsig.com/product/vibratone-bells',
    # 'https://signaling.fedsig.com/product/pmlmp-pmlst',
    # 'https://signaling.fedsig.com/product/g-snd-sounder',
    # 'https://signaling.fedsig.com/product/g-spa-speaker',
    # 'https://signaling.fedsig.com/product/radiant-stack-light',
    # 'https://signaling.fedsig.com/product/g-spk-louderspeaker',
    # 'https://signaling.fedsig.com/product/LSB-024-240',
    # 'https://signaling.fedsig.com/product/LSB-120',
    # 'https://signaling.fedsig.com/product/lp4-mini-sounder',
    # 'https://signaling.fedsig.com/product/LSBS',
    # 'https://signaling.fedsig.com/product/lsh-lifestak-horn',
    # 'https://signaling.fedsig.com/product/model-a-general-alarm-siren',
    # 'https://signaling.fedsig.com/product/lsld-litestak-led',
    # 'https://signaling.fedsig.com/product/model-l-general-alarm-siren',
    # 'https://signaling.fedsig.com/product/MSP-16',
    # 'https://signaling.fedsig.com/product/MSP-32',
    # 'https://signaling.fedsig.com/product/MSP-4',
    # 'https://signaling.fedsig.com/product/MSS-024',
    # 'https://signaling.fedsig.com/product/MSS-120',
    # 'https://signaling.fedsig.com/product/pma-pmamt',
    # 'https://signaling.fedsig.com/product/MSTB',
    # 'https://signaling.fedsig.com/product/ps250-ps600-ps1000',
    # 'https://signaling.fedsig.com/product/LCMB2',
    # 'https://signaling.fedsig.com/product/selectone-overview',
    # 'https://signaling.fedsig.com/product/LHWB',
    # 'https://signaling.fedsig.com/product/selectone-connector-kits',
    # 'https://signaling.fedsig.com/product/slm700',
    # 'https://signaling.fedsig.com/product/LSWB',
    # 'https://signaling.fedsig.com/product/slm800',
    # 'https://signaling.fedsig.com/product/LWMB2',
    # 'https://signaling.fedsig.com/product/slmb',
    # 'https://signaling.fedsig.com/product/MSLBRCKT',
    # 'https://signaling.fedsig.com/product/slmbd',
    # 'https://signaling.fedsig.com/product/slmbp',
    # 'https://signaling.fedsig.com/product/black-mounting-kits',
    # 'https://signaling.fedsig.com/product/red-mounting-kits',
    # 'https://signaling.fedsig.com/product/slmbs',
    # 'https://signaling.fedsig.com/product/slmbt',
    # 'https://signaling.fedsig.com/product/slmbw',
    # 'https://signaling.fedsig.com/product/EHORN-TKIT',
    # 'https://signaling.fedsig.com/product/ESIREN-SKIT',
    # 'https://signaling.fedsig.com/product/EVL-120',
    # 'https://signaling.fedsig.com/product/EVS-120',
    # 'https://signaling.fedsig.com/product/FB',
    # 'https://signaling.fedsig.com/product/FBL',
    # 'https://signaling.fedsig.com/product/FG',
    # 'https://signaling.fedsig.com/product/G-KIT-DT',
    # 'https://signaling.fedsig.com/product/semistat-status-indicator',
    # 'https://signaling.fedsig.com/product/G-KIT-EC180',
    # 'https://signaling.fedsig.com/product/G-KIT-EC90',
    # 'https://signaling.fedsig.com/product/slm100-streamline',
    # 'https://signaling.fedsig.com/product/G-KIT-ECSM',
    # 'https://signaling.fedsig.com/product/slm1400-slm1450-streamline',
    # 'https://signaling.fedsig.com/product/slm200-streamline',
    # 'https://signaling.fedsig.com/product/G-KIT-EXTB',
    # 'https://signaling.fedsig.com/product/g-kit-rp',
    # 'https://signaling.fedsig.com/product/G-KIT-ST',
    # 'https://signaling.fedsig.com/product/K14702254A',
    # 'https://signaling.fedsig.com/product/slm500-streamline',
    # 'https://signaling.fedsig.com/product/slm600-streamline',
    # 'https://signaling.fedsig.com/product/KIT-WBTB',
    # 'https://signaling.fedsig.com/product/SLMB23N',
    # 'https://signaling.fedsig.com/product/MNC-1',
    # 'https://signaling.fedsig.com/product/SLMB23V',
    # 'https://signaling.fedsig.com/product/MNC-MC',
    # 'https://signaling.fedsig.com/product/SLMB23W',
    # 'https://signaling.fedsig.com/product/MSB-1',
    # 'https://signaling.fedsig.com/product/PR2-NM',
    # 'https://signaling.fedsig.com/product/SLMDG0',
    # 'https://signaling.fedsig.com/product/RM1SD',
    # 'https://signaling.fedsig.com/product/SLMDG1',
    # 'https://signaling.fedsig.com/product/RMB9999SD',
    # 'https://signaling.fedsig.com/product/SLMDG3',
    # 'https://signaling.fedsig.com/product/WB',
    # 'https://signaling.fedsig.com/product/K120846A',
    # 'https://signaling.fedsig.com/product/A1779S',
    # 'https://signaling.fedsig.com/product/K120856A',
    # 'https://signaling.fedsig.com/product/A2133S',
    # 'https://signaling.fedsig.com/product/A3410S',
    # 'https://signaling.fedsig.com/product/K120857A',
    # 'https://signaling.fedsig.com/product/K120858A',
    # 'https://signaling.fedsig.com/product/K124095A',
    # 'https://signaling.fedsig.com/product/K1461647A',
    # 'https://signaling.fedsig.com/product/K120B255A',
    # 'https://signaling.fedsig.com/product/K146A986A',
    # 'https://signaling.fedsig.com/product/K125165A',
    # 'https://signaling.fedsig.com/product/K139A209B',
    # 'https://signaling.fedsig.com/product/K14700030A-A',
    # 'https://signaling.fedsig.com/product/K14700030A-B',
    # 'https://signaling.fedsig.com/product/K140340B',
    # 'https://signaling.fedsig.com/product/K140373A-02',
    # 'https://signaling.fedsig.com/product/K14700030A-G',
    # 'https://signaling.fedsig.com/product/K140373A-03',
    # 'https://signaling.fedsig.com/product/K14700030A-R',
    # 'https://signaling.fedsig.com/product/K140373A-05',
    # 'https://signaling.fedsig.com/product/K14700030A-W',
    # 'https://signaling.fedsig.com/product/K140373A-08',
    # 'https://signaling.fedsig.com/product/K14700030A-Y',
    # 'https://signaling.fedsig.com/product/K148176A',
    # 'https://signaling.fedsig.com/product/K140389A-03',
    # 'https://signaling.fedsig.com/product/K140389A-04',
    # 'https://signaling.fedsig.com/product/K148A133A',
    # 'https://signaling.fedsig.com/product/K149122B',
    # 'https://signaling.fedsig.com/product/K140411A-03',
    # 'https://signaling.fedsig.com/product/K140A332A-10',
    # 'https://signaling.fedsig.com/product/K149123A',
    # 'https://signaling.fedsig.com/product/K140A332A-16',
    # 'https://signaling.fedsig.com/product/K149128A',
    # 'https://signaling.fedsig.com/product/K140A332A-17',
    # 'https://signaling.fedsig.com/product/K149130A',
    # 'https://signaling.fedsig.com/product/K149133A',
    # 'https://signaling.fedsig.com/product/K155189A',
    # 'https://signaling.fedsig.com/product/K155190A',
    # 'https://signaling.fedsig.com/product/K150159A',
    # 'https://signaling.fedsig.com/product/K2001071B',
    # 'https://signaling.fedsig.com/product/K170455A-07',
    # 'https://signaling.fedsig.com/product/K2001071B-01',
    # 'https://signaling.fedsig.com/product/K1751021A',
    # 'https://signaling.fedsig.com/product/K20000104A',
    # 'https://signaling.fedsig.com/product/K2001202C',
    # 'https://signaling.fedsig.com/product/K2001147A',
    # 'https://signaling.fedsig.com/product/K2001202C-01',
    # 'https://signaling.fedsig.com/product/K2001154E',
    # 'https://signaling.fedsig.com/product/K2001164A',
    # 'https://signaling.fedsig.com/product/K2001227E',
    # 'https://signaling.fedsig.com/product/K2001265D-01',
    # 'https://signaling.fedsig.com/product/K2001312A',
    # 'https://signaling.fedsig.com/product/K2001887A-02',
    # 'https://signaling.fedsig.com/product/K2001888C',
    # 'https://signaling.fedsig.com/product/K2001905A',
    # 'https://signaling.fedsig.com/product/K2001903B',
    # 'https://signaling.fedsig.com/product/K2001905A-01',
    # 'https://signaling.fedsig.com/product/K2001918B',
    # 'https://signaling.fedsig.com/product/K2001961B-02',
    # 'https://signaling.fedsig.com/product/K2001918B-01',
    # 'https://signaling.fedsig.com/product/K2001961B-04',
    # 'https://signaling.fedsig.com/product/K2001921B-02',
    # 'https://signaling.fedsig.com/product/K2001961B-05',
    # 'https://signaling.fedsig.com/product/K2001921B-03',
    # 'https://signaling.fedsig.com/product/K2005110A',
    # 'https://signaling.fedsig.com/product/K2001921B-04',
    # 'https://signaling.fedsig.com/product/K2005618A-01',
    # 'https://signaling.fedsig.com/product/K2001921B-05',
    # 'https://signaling.fedsig.com/product/K2005618A-02',
    # 'https://signaling.fedsig.com/product/K2001921B-06',
    # 'https://signaling.fedsig.com/product/K200A508',
    # 'https://signaling.fedsig.com/product/K2001921B-07',
    # 'https://signaling.fedsig.com/product/K200A792E',
    # 'https://signaling.fedsig.com/product/K200B461',
    # 'https://signaling.fedsig.com/product/K2001921B-08',
    # 'https://signaling.fedsig.com/product/K200D1148H',
    # 'https://signaling.fedsig.com/product/K2001925A',
    # 'https://signaling.fedsig.com/product/K2001925A-01',
    # 'https://signaling.fedsig.com/product/K229277A',
    # 'https://signaling.fedsig.com/product/K2001925A-02',
    # 'https://signaling.fedsig.com/product/K229277A-01',
    # 'https://signaling.fedsig.com/product/K2001925A-03',
    # 'https://signaling.fedsig.com/product/K231246A',
    # 'https://signaling.fedsig.com/product/K2001926A-03',
    # 'https://signaling.fedsig.com/product/K231247',
    # 'https://signaling.fedsig.com/product/K2001961B',
    # 'https://signaling.fedsig.com/product/K2881076A-03',
    # 'https://signaling.fedsig.com/product/K288920A',
    # 'https://signaling.fedsig.com/product/K2001961B-01',
    # 'https://signaling.fedsig.com/product/K288921A',
    # 'https://signaling.fedsig.com/product/K2001961B-03',
    # 'https://signaling.fedsig.com/product/K2001966A',
    # 'https://signaling.fedsig.com/product/K288A043',
    # 'https://signaling.fedsig.com/product/K2005328A',
    # 'https://signaling.fedsig.com/product/K288A542A',
    # 'https://signaling.fedsig.com/product/K2005328A-01',
    # 'https://signaling.fedsig.com/product/K77700379',
    # 'https://signaling.fedsig.com/product/K2005360A',
    # 'https://signaling.fedsig.com/product/K8006007A',
    # 'https://signaling.fedsig.com/product/K2005366A',
    # 'https://signaling.fedsig.com/product/K8118052A',
    # 'https://signaling.fedsig.com/product/K2005416A',
    # 'https://signaling.fedsig.com/product/K8233107A-01',
    # 'https://signaling.fedsig.com/product/K8233A046-0G',
    # 'https://signaling.fedsig.com/product/K2005416A-01',
    # 'https://signaling.fedsig.com/product/K8242C007-01',
    # 'https://signaling.fedsig.com/product/K8242C007-02',
    # 'https://signaling.fedsig.com/product/K8242D006-01',
    # 'https://signaling.fedsig.com/product/K2005455A',
    # 'https://signaling.fedsig.com/product/K8242D006-02',
    # 'https://signaling.fedsig.com/product/K2005502A-01',
    # 'https://signaling.fedsig.com/product/K82831051A',
    # 'https://signaling.fedsig.com/product/K2005502A-02',
    # 'https://signaling.fedsig.com/product/K8283A700',
    # 'https://signaling.fedsig.com/product/K2005502A-04',
    # 'https://signaling.fedsig.com/product/K8283B430-01',
    # 'https://signaling.fedsig.com/product/K2005618A-03',
    # 'https://signaling.fedsig.com/product/K8283C071-0G',
    # 'https://signaling.fedsig.com/product/K2005618A-04',
    # 'https://signaling.fedsig.com/product/K2005618A-05',
    # 'https://signaling.fedsig.com/product/K8435663B',
    # 'https://signaling.fedsig.com/product/K8435696A',
    # 'https://signaling.fedsig.com/product/K2005618A-06',
    # 'https://signaling.fedsig.com/product/K2005633A-A',
    # 'https://signaling.fedsig.com/product/K2005633A-B',
    # 'https://signaling.fedsig.com/product/K2005633A-G',
    # 'https://signaling.fedsig.com/product/K8459108A',
    # 'https://signaling.fedsig.com/product/K2005633A-R',
    # 'https://signaling.fedsig.com/product/K8459109B',
    # 'https://signaling.fedsig.com/product/K2005633A-W',
    # 'https://signaling.fedsig.com/product/K2005642A',
    # 'https://signaling.fedsig.com/product/K8468A056',
    # 'https://signaling.fedsig.com/product/K8473021A',
    # 'https://signaling.fedsig.com/product/K2005695A',
    # 'https://signaling.fedsig.com/product/K2005777A-M34',
    # 'https://signaling.fedsig.com/product/K8473022A',
    # 'https://signaling.fedsig.com/product/K200865G',
    # 'https://signaling.fedsig.com/product/K8473B006',
    # 'https://signaling.fedsig.com/product/K8476121A',
    # 'https://signaling.fedsig.com/product/K200865G-02',
    # 'https://signaling.fedsig.com/product/K200D866G',
    # 'https://signaling.fedsig.com/product/K8476121A-04',
    # 'https://signaling.fedsig.com/product/K200D866G-01',
    # 'https://signaling.fedsig.com/product/K8476122A',
    # 'https://signaling.fedsig.com/product/K201072B',
    # 'https://signaling.fedsig.com/product/K8476123A',
    # 'https://signaling.fedsig.com/product/K201073B',
    # 'https://signaling.fedsig.com/product/K8476C043A-01',
    # 'https://signaling.fedsig.com/product/K201074B',
    # 'https://signaling.fedsig.com/product/K8502110A',
    # 'https://signaling.fedsig.com/product/K8502A006A',
    # 'https://signaling.fedsig.com/product/K201075B',
    # 'https://signaling.fedsig.com/product/K201076B',
    # 'https://signaling.fedsig.com/product/K8504002A',
    # 'https://signaling.fedsig.com/product/K8590050A',
    # 'https://signaling.fedsig.com/product/K201077B',
    # 'https://signaling.fedsig.com/product/K201078B',
    # 'https://signaling.fedsig.com/product/K8590243A',
    # 'https://signaling.fedsig.com/product/K8590246A',
    # 'https://signaling.fedsig.com/product/K201080B',
    # 'https://signaling.fedsig.com/product/K201080B-01',
    # 'https://signaling.fedsig.com/product/K8590249A',
    # 'https://signaling.fedsig.com/product/K8591002A',
    # 'https://signaling.fedsig.com/product/K201081B',
    # 'https://signaling.fedsig.com/product/K8591002A-02',
    # 'https://signaling.fedsig.com/product/K201081B-01',
    # 'https://signaling.fedsig.com/product/K8593035A',
    # 'https://signaling.fedsig.com/product/K201081B-02',
    # 'https://signaling.fedsig.com/product/K8593071A',
    # 'https://signaling.fedsig.com/product/K201082A',
    # 'https://signaling.fedsig.com/product/K201084A',
    # 'https://signaling.fedsig.com/product/K8593082A',
    # 'https://signaling.fedsig.com/product/K8593100A',
    # 'https://signaling.fedsig.com/product/K201173A',
    # 'https://signaling.fedsig.com/product/K201187A',
    # 'https://signaling.fedsig.com/product/K8593100A-01',
    # 'https://signaling.fedsig.com/product/K8593101A',
    # 'https://signaling.fedsig.com/product/K201189A',
    # 'https://signaling.fedsig.com/product/K8593103A',
    # 'https://signaling.fedsig.com/product/K231305A',
    # 'https://signaling.fedsig.com/product/K2881358A',
    # 'https://signaling.fedsig.com/product/K8593103A-01',
    # 'https://signaling.fedsig.com/product/K288698A',
    # 'https://signaling.fedsig.com/product/K859500361A',
    # 'https://signaling.fedsig.com/product/K859500805-01',
    # 'https://signaling.fedsig.com/product/K288699A',
    # 'https://signaling.fedsig.com/product/K288801A',
    # 'https://signaling.fedsig.com/product/K859500805-02',
    # 'https://signaling.fedsig.com/product/K859500874',
    # 'https://signaling.fedsig.com/product/K859501176',
    # 'https://signaling.fedsig.com/product/K77700416',
    # 'https://signaling.fedsig.com/product/K859501403',
    # 'https://signaling.fedsig.com/product/K77700416-01',
    # 'https://signaling.fedsig.com/product/K8004141A-01',
    # 'https://signaling.fedsig.com/product/K859501404',
    # 'https://signaling.fedsig.com/product/K8006009A',
    # 'https://signaling.fedsig.com/product/K859501405-070',
    # 'https://signaling.fedsig.com/product/K859501405-100',
    # 'https://signaling.fedsig.com/product/K8006029A',
    # 'https://signaling.fedsig.com/product/K859501414',
    # 'https://signaling.fedsig.com/product/K8107159A',
    # 'https://signaling.fedsig.com/product/K8107177A',
    # 'https://signaling.fedsig.com/product/K8595143A',
    # 'https://signaling.fedsig.com/product/K8107178A',
    # 'https://signaling.fedsig.com/product/K8595150A',
    # 'https://signaling.fedsig.com/product/K8595151A',
    # 'https://signaling.fedsig.com/product/K8107185A',
    # 'https://signaling.fedsig.com/product/K8595153A',
    # 'https://signaling.fedsig.com/product/K8107194A',
    # 'https://signaling.fedsig.com/product/K8595171A',
    # 'https://signaling.fedsig.com/product/K8595172A',
    # 'https://signaling.fedsig.com/product/K8107194A-25',
    # 'https://signaling.fedsig.com/product/K8597108A',
    # 'https://signaling.fedsig.com/product/K8107194A-4',
    # 'https://signaling.fedsig.com/product/K8597165A',
    # 'https://signaling.fedsig.com/product/K8107199A',
    # 'https://signaling.fedsig.com/product/K8597168A',
    # 'https://signaling.fedsig.com/product/K8597198A',
    # 'https://signaling.fedsig.com/product/K8107199A-01',
    # 'https://signaling.fedsig.com/product/K8107199A-02',
    # 'https://signaling.fedsig.com/product/K8597201A',
    # 'https://signaling.fedsig.com/product/K8601245A',
    # 'https://signaling.fedsig.com/product/K8107199A-03',
    # 'https://signaling.fedsig.com/product/K8107199A-04',
    # 'https://signaling.fedsig.com/product/K8107200A',
    # 'https://signaling.fedsig.com/product/KFC1516C',
    # 'https://signaling.fedsig.com/product/K8107200A-01',
    # 'https://signaling.fedsig.com/product/K8107200A-02',
    # 'https://signaling.fedsig.com/product/K8107200A-03',
    # 'https://signaling.fedsig.com/product/K8107200A-04',
    # 'https://signaling.fedsig.com/product/K8107210A',
    # 'https://signaling.fedsig.com/product/KH314',
    # 'https://signaling.fedsig.com/product/KH5359L-0A-0G',
    # 'https://signaling.fedsig.com/product/K8107213A',
    # 'https://signaling.fedsig.com/product/KH6962J-01',
    # 'https://signaling.fedsig.com/product/KH6962J-02',
    # 'https://signaling.fedsig.com/product/KH7999F-02',
    # 'https://signaling.fedsig.com/product/K8107A041',
    # 'https://signaling.fedsig.com/product/K8107A149A',
    # 'https://signaling.fedsig.com/product/K8107A151A',
    # 'https://signaling.fedsig.com/product/K8118C023',
    # 'https://signaling.fedsig.com/product/K8228A032A-S',
    # 'https://signaling.fedsig.com/product/K8233A021',
    # 'https://signaling.fedsig.com/product/K8234A008-01',
    # 'https://signaling.fedsig.com/product/K8241A014B',
    # 'https://signaling.fedsig.com/product/K8263079A',
    # 'https://signaling.fedsig.com/product/K8263079A-01',
    # 'https://signaling.fedsig.com/product/K8263079A-02',
    # 'https://signaling.fedsig.com/product/K8263079A-03',
    # 'https://signaling.fedsig.com/product/K8263079A-04',
    # 'https://signaling.fedsig.com/product/K8283A689',
    # 'https://signaling.fedsig.com/product/K8283C431-0R',
    # 'https://signaling.fedsig.com/product/K8285237A',
    # 'https://signaling.fedsig.com/product/K8285237A-01',
    # 'https://signaling.fedsig.com/product/K8285238A-01',
    # 'https://signaling.fedsig.com/product/K8285239A',
    # 'https://signaling.fedsig.com/product/K8422B428A',
    # 'https://signaling.fedsig.com/product/K8422B428A-01',
    # 'https://signaling.fedsig.com/product/K8422B428A-02',
    # 'https://signaling.fedsig.com/product/K8422B428A-03',
    # 'https://signaling.fedsig.com/product/K8422B428A-04',
    # 'https://signaling.fedsig.com/product/K8435666A',
    # 'https://signaling.fedsig.com/product/K8435711A',
    # 'https://signaling.fedsig.com/product/K8435711A-01',
    # 'https://signaling.fedsig.com/product/K8435711A-02',
    # 'https://signaling.fedsig.com/product/K8435711A-03',
    # 'https://signaling.fedsig.com/product/K8435711A-04',
    # 'https://signaling.fedsig.com/product/K8435A130',
    # 'https://signaling.fedsig.com/product/K8436107E-02',
    # 'https://signaling.fedsig.com/product/K8436107F-03',
    # 'https://signaling.fedsig.com/product/K8436107F-05',
    # 'https://signaling.fedsig.com/product/K8436147A',
    # 'https://signaling.fedsig.com/product/K8436147A-01',
    # 'https://signaling.fedsig.com/product/K8444255A-01',
    # 'https://signaling.fedsig.com/product/K8444269A',
    # 'https://signaling.fedsig.com/product/K8444269A-01',
    # 'https://signaling.fedsig.com/product/K8444269A-02',
    # 'https://signaling.fedsig.com/product/K8444269A-03',
    # 'https://signaling.fedsig.com/product/K8444269A-04',
    # 'https://signaling.fedsig.com/product/K8444286B',
    # 'https://signaling.fedsig.com/product/K8444356A',
    # 'https://signaling.fedsig.com/product/K8444357A',
    # 'https://signaling.fedsig.com/product/K8444357A-01',
    # 'https://signaling.fedsig.com/product/K8444357A-02',
    # 'https://signaling.fedsig.com/product/K8444357A-03',
    # 'https://signaling.fedsig.com/product/K8444357A-04',
    # 'https://signaling.fedsig.com/product/K8444357A-05',
    # 'https://signaling.fedsig.com/product/K8444A211B',
    # 'https://signaling.fedsig.com/product/K8444D218B',
    # 'https://signaling.fedsig.com/product/K8444D219C',
    # 'https://signaling.fedsig.com/product/K8444D219C-01',
    # 'https://signaling.fedsig.com/product/K8444D219C-02',
    # 'https://signaling.fedsig.com/product/K8444D219C-03',
    # 'https://signaling.fedsig.com/product/K8444D219C-04',
    # 'https://signaling.fedsig.com/product/K844700351A',
    # 'https://signaling.fedsig.com/product/K844700352A',
    # 'https://signaling.fedsig.com/product/K8447003B',
    # 'https://signaling.fedsig.com/product/K8447043B',
    # 'https://signaling.fedsig.com/product/K8447044A-02',
    # 'https://signaling.fedsig.com/product/K8447143A',
    # 'https://signaling.fedsig.com/product/K8447158A',
    # 'https://signaling.fedsig.com/product/K8447159A',
    # 'https://signaling.fedsig.com/product/K8449078C',
    # 'https://signaling.fedsig.com/product/K8449078C-01',
    # 'https://signaling.fedsig.com/product/K8449078C-04',
    # 'https://signaling.fedsig.com/product/K8449078C-05',
    # 'https://signaling.fedsig.com/product/K8449078C-06',
    # 'https://signaling.fedsig.com/product/K8449078C-07',
    # 'https://signaling.fedsig.com/product/K8449121A',
    # 'https://signaling.fedsig.com/product/K8449C005-11',
    # 'https://signaling.fedsig.com/product/K8449C005-12',
    # 'https://signaling.fedsig.com/product/K8449C005-13',
    # 'https://signaling.fedsig.com/product/K8449C005-14',
    # 'https://signaling.fedsig.com/product/K8449C005-15',
    # 'https://signaling.fedsig.com/product/K8459123A',
    # 'https://signaling.fedsig.com/product/K8459125A',
    # 'https://signaling.fedsig.com/product/K8459125A-01',
    # 'https://signaling.fedsig.com/product/K8459125A-02',
    # 'https://signaling.fedsig.com/product/K8459125A-03',
    # 'https://signaling.fedsig.com/product/K8459125A-04',
    # 'https://signaling.fedsig.com/product/K8459127A',
    # 'https://signaling.fedsig.com/product/K8459130A',
    # 'https://signaling.fedsig.com/product/K8459138A',
    # 'https://signaling.fedsig.com/product/K8459159A-A',
    # 'https://signaling.fedsig.com/product/K8459159A-B',
    # 'https://signaling.fedsig.com/product/K8459159A-G',
    # 'https://signaling.fedsig.com/product/K8459159A-R',
    # 'https://signaling.fedsig.com/product/K8459159A-W',
    # 'https://signaling.fedsig.com/product/K8459A076C',
    # 'https://signaling.fedsig.com/product/K8505037B',
    # 'https://signaling.fedsig.com/product/K8550292A',
    # 'https://signaling.fedsig.com/product/K8550292A-01',
    # 'https://signaling.fedsig.com/product/K8550292A-02',
    # 'https://signaling.fedsig.com/product/K8550292A-03',
    # 'https://signaling.fedsig.com/product/K8550292A-04',
    # 'https://signaling.fedsig.com/product/K8550292A-05',
    # 'https://signaling.fedsig.com/product/K8550320A',
    # 'https://signaling.fedsig.com/product/K8550320A-01',
    # 'https://signaling.fedsig.com/product/K8550320A-02',
    # 'https://signaling.fedsig.com/product/K8550320A-03',
    'https://signaling.fedsig.com/product/K8550320A-04',
    'https://signaling.fedsig.com/product/K8550320A-05',
    'https://signaling.fedsig.com/product/K8550326A',
    'https://signaling.fedsig.com/product/K8550333A',
    'https://signaling.fedsig.com/product/K8550C095A',
    'https://signaling.fedsig.com/product/K8550C095A-01',
    'https://signaling.fedsig.com/product/K8550C095A-02',
    'https://signaling.fedsig.com/product/K8550C095A-03',
    'https://signaling.fedsig.com/product/K8550C095A-04',
    'https://signaling.fedsig.com/product/K8550C095A-07',
    'https://signaling.fedsig.com/product/K858900353A',
    'https://signaling.fedsig.com/product/K8589037A',
    'https://signaling.fedsig.com/product/K8589037A-01',
    'https://signaling.fedsig.com/product/K8589037A-02',
    'https://signaling.fedsig.com/product/K8589037A-03',
    'https://signaling.fedsig.com/product/K8589037A-04',
    'https://signaling.fedsig.com/product/K8589058A',
    'https://signaling.fedsig.com/product/K8589063A',
    'https://signaling.fedsig.com/product/K8589063A-01',
    'https://signaling.fedsig.com/product/K8589063A-02',
    'https://signaling.fedsig.com/product/K8589063A-03',
    'https://signaling.fedsig.com/product/K8589063A-04',
    'https://signaling.fedsig.com/product/K8590242A',
    'https://signaling.fedsig.com/product/K8590246A-01',
    'https://signaling.fedsig.com/product/K8590288A',
    'https://signaling.fedsig.com/product/K8590298A',
    'https://signaling.fedsig.com/product/K8591002A-03',
    'https://signaling.fedsig.com/product/K859500809',
    'https://signaling.fedsig.com/product/K859500814',
    'https://signaling.fedsig.com/product/K859500814-01',
    'https://signaling.fedsig.com/product/K859500814-02',
    'https://signaling.fedsig.com/product/K859500814-03',
    'https://signaling.fedsig.com/product/K859500814-04',
    'https://signaling.fedsig.com/product/K859500814-05',
    'https://signaling.fedsig.com/product/K859500814-06',
    'https://signaling.fedsig.com/product/K859500815',
    'https://signaling.fedsig.com/product/K859500815-01',
    'https://signaling.fedsig.com/product/K859500815-02',
    'https://signaling.fedsig.com/product/K859500815-03',
    'https://signaling.fedsig.com/product/K859500815-04',
    'https://signaling.fedsig.com/product/K859500815-05',
    'https://signaling.fedsig.com/product/K859500815-06',
    'https://signaling.fedsig.com/product/K859500821-01',
    'https://signaling.fedsig.com/product/K859500821-02',
    'https://signaling.fedsig.com/product/K859501178',
    'https://signaling.fedsig.com/product/K859501180',
    'https://signaling.fedsig.com/product/K859501227',
    'https://signaling.fedsig.com/product/K859501400-A',
    'https://signaling.fedsig.com/product/K859501400-B',
    'https://signaling.fedsig.com/product/K859501400-G',
    'https://signaling.fedsig.com/product/K859501400-R',
    'https://signaling.fedsig.com/product/K859501400-W',
    'https://signaling.fedsig.com/product/K859501401-A',
    'https://signaling.fedsig.com/product/K859501401-B',
    'https://signaling.fedsig.com/product/K859501401-G',
    'https://signaling.fedsig.com/product/K859501401-R',
    'https://signaling.fedsig.com/product/K859501401-W',
    'https://signaling.fedsig.com/product/K859501402-024',
    'https://signaling.fedsig.com/product/K859501402-120',
    'https://signaling.fedsig.com/product/K859501402-230',
    'https://signaling.fedsig.com/product/K8595116A-AA',
    'https://signaling.fedsig.com/product/K8595116A-CA',
    'https://signaling.fedsig.com/product/K8595116A-LB',
    'https://signaling.fedsig.com/product/K8595116A-LG',
    'https://signaling.fedsig.com/product/K8595116A-RA',
    'https://signaling.fedsig.com/product/K8595116A-YA',
    'https://signaling.fedsig.com/product/K8595177A',
    'https://signaling.fedsig.com/product/K8597129A',
    'https://signaling.fedsig.com/product/K8597134A',
    'https://signaling.fedsig.com/product/K8597206A',
    'https://signaling.fedsig.com/product/K14702196A',
    'https://signaling.fedsig.com/product/pm22l-rgb',
    'https://signaling.fedsig.com/product/commercial-vehicle-backup-alarm-IS-210239-S',
    'https://signaling.fedsig.com/product/Z865300732',
    'https://signaling.fedsig.com/product/300B-TALL',
    'https://signaling.fedsig.com/product/radiant-steady-light-module',
    'https://signaling.fedsig.com/product/IPX-PBL1',
    'https://signaling.fedsig.com/product/K8449090C',
    'https://signaling.fedsig.com/product/pm22c-rgb',
    'https://signaling.fedsig.com/product/Z1751531A',
    'https://signaling.fedsig.com/product/pm22l',
    'https://signaling.fedsig.com/product/pm22a',
    'https://signaling.fedsig.com/product/pm22c',
    'https://signaling.fedsig.com/product/200775-95',
    'https://signaling.fedsig.com/product/radiant-multi-pattern-light-module',
    'https://signaling.fedsig.com/product/G-KIT-15WINSERT',
    'https://signaling.fedsig.com/product/radiant-sound-module',
    'https://signaling.fedsig.com/product/radiant-wiring-modules',
    'https://signaling.fedsig.com/product/K8444277A',
    'https://signaling.fedsig.com/product/AV-CK',
    'https://signaling.fedsig.com/product/K8444277A-01',
    'https://signaling.fedsig.com/product/K8444277A-02',
    'https://signaling.fedsig.com/product/K8444277A-03',
    'https://signaling.fedsig.com/product/K8444277A-04',
    'https://signaling.fedsig.com/product/msl-led',
    'https://signaling.fedsig.com/product/2000-series-xen1-xen4',
    'https://signaling.fedsig.com/product/atkinson-dynamics-non-amplified-speaker',
    'https://signaling.fedsig.com/product/K101216A',
    'https://signaling.fedsig.com/product/224xst-electraray',
    'https://signaling.fedsig.com/product/300x-selectone',
    'https://signaling.fedsig.com/product/224xsthi-electraray',
    'https://signaling.fedsig.com/product/302gc-selectone',
    'https://signaling.fedsig.com/product/K122339A',
    'https://signaling.fedsig.com/product/K122A298A',
    'https://signaling.fedsig.com/product/302gcx-cn-selectone',
    'https://signaling.fedsig.com/product/225-rotating-light',
    'https://signaling.fedsig.com/product/K131220A',
    'https://signaling.fedsig.com/product/225x-electraray-rotating-light',
    'https://signaling.fedsig.com/product/302gcx-selectone',
    'https://signaling.fedsig.com/product/K137144A',
    'https://signaling.fedsig.com/product/225xl-electraray-led',
    'https://signaling.fedsig.com/product/302x-selectone',
    'https://signaling.fedsig.com/product/K140A326A-01',
    'https://signaling.fedsig.com/product/225xl-n-nsf-series',
    'https://signaling.fedsig.com/product/304gc-314gc',
    'https://signaling.fedsig.com/product/304gcx-314gcx',
    'https://signaling.fedsig.com/product/K141133A',
    'https://signaling.fedsig.com/product/225xst-i',
    'https://signaling.fedsig.com/product/g-led-global-series',
    'https://signaling.fedsig.com/product/g-msc-custom-global-series',
    'https://signaling.fedsig.com/product/g-msc-global-series',
    'https://signaling.fedsig.com/product/g-str-global-series',
    'https://signaling.fedsig.com/product/usi-status-indicator',
    'https://signaling.fedsig.com/product/usix-hazardous-status-indicator',
    'https://signaling.fedsig.com/product/radiant-mounting-options',
    'https://signaling.fedsig.com/product/radiant-steady-bright-light-module',
    'https://signaling.fedsig.com/product/fb2led-fireball-led',
    'https://signaling.fedsig.com/product/fb2ledx-fireball',
    'https://signaling.fedsig.com/product/vlbl',
    'https://signaling.fedsig.com/product/fb24st-fireball-strobe',
    'https://signaling.fedsig.com/product/fb24sthi-fireball-supervised-strobe-light',
    'https://signaling.fedsig.com/product/fb2pst-fireball',
    'https://signaling.fedsig.com/product/fb2pst-i-fireball',
    'https://signaling.fedsig.com/product/fsex',
    'https://signaling.fedsig.com/product/fsex-hi',
    'https://signaling.fedsig.com/product/DBLP',
    'https://signaling.fedsig.com/product/DGXC-SB',
    'https://signaling.fedsig.com/product/FB2G',
    'https://signaling.fedsig.com/product/ehorn',
    'https://signaling.fedsig.com/product/ehorn-hv',
    'https://signaling.fedsig.com/product/ashh-asuh',
    'https://signaling.fedsig.com/product/ashp-asup',
    'https://signaling.fedsig.com/product/ashx-asux',
    'https://signaling.fedsig.com/product/em3-selectone-extension-module',
    'https://signaling.fedsig.com/product/cts2-amplifiers',
    'https://signaling.fedsig.com/product/audiomaster-public-address-speaker-am30',
    'https://signaling.fedsig.com/product/am300-am302',
    'https://signaling.fedsig.com/product/am300gcx-am302gcx',
    'https://signaling.fedsig.com/product/am300x-am302x',
    'https://signaling.fedsig.com/product/audiomaster-public-address-transformer-am30t',
    'https://signaling.fedsig.com/product/am50-audiomaster',
    'https://signaling.fedsig.com/product/amr6-audiomaster',
    'https://signaling.fedsig.com/product/K288697A',
    'https://signaling.fedsig.com/product/K288696A',
    'https://signaling.fedsig.com/product/K8590013B',
    'https://signaling.fedsig.com/product/K8590013B-01',
    'https://signaling.fedsig.com/product/K8590236A',
    'https://signaling.fedsig.com/product/K8590237A',
    'https://signaling.fedsig.com/product/K8590239B',
    'https://signaling.fedsig.com/product/K8590241A',
    'https://signaling.fedsig.com/product/K8590287A',
    'https://signaling.fedsig.com/product/SLMNPT1',
    'https://signaling.fedsig.com/product/SLMNPT2',
    'https://signaling.fedsig.com/product/SLM-RR',
    'https://signaling.fedsig.com/product/SSM',

]
for url in mylist:
    l = l + 1
    driver.get(url)
    driver.get(driver.current_url)
    time.sleep(12)
    print("Products Urls", l, url)

    title_d = ''
    sku_d = ''
    Description_d = ''
    feature_d = ''
    price_d = ''
    pdf_d = ''
    option_d = ''
    # =================================================== Find breadcrumb =============================================
    Breadcrumb_d = []
    print("*********************************** Breadcrumb : **************************************")
    Breadcrumb = driver.find_elements(By.ID, 'breadcrumbElement')
    for x in Breadcrumb:
        Breadcrumb_d.append(x.text)
    print("Breadcrumb = ", Breadcrumb_d)
    try:
        # ================================================ find title =====================================================
        print("***********************************  Title : **************************************")
        title = driver.find_element(By.CLASS_NAME, 'visible-lg')
        title_d = title.text
        print("title = ", title_d)
    except:
        print("Not Found")

    try:
        print('*********************** First Options *************************')
        all_options = driver.find_element(By.ID, 'wi700851-fs-product-variants-id').find_elements(By.TAG_NAME, 'option')
        op = []
        for o in all_options:
            # print("options = ", o.text)
            if "..." not in o.text:
                op.append(o.text)
        # print(op)
        dropdown = Select(driver.find_element(By.CLASS_NAME, 'cc-skuDropdown'))
        input1 = len(dropdown.options)
        # print("inputs = ", input1)

        for option, item in zip(op, range(1, input1)):
            time.sleep(3)
            dropdown = Select(driver.find_element(By.CLASS_NAME, 'cc-skuDropdown'))
            print("first loop = ", item)
            dropdown.select_by_index(item)
            option_d = option
            print("options = ", option_d)
            time.sleep(3)

            try:
                print("************************************* Price : ****************************************")
                price = driver.find_element(By.ID, 'wi700851-fs-product-list-price-id')
                price_d = price.text
                print("Price = ", price_d)
            except:
                price_d = "Not Found"
                print("Not Found Price")
            try:
                print("************************************* sku : ****************************************")
                sku = driver.find_element(By.CLASS_NAME, 'cc-sku')
                sku_d = sku.text
                print("sku = ", sku_d)
                save_details: TextIO = open("main_files.xlsx", "a+", encoding="utf-8")
                save_details.write("\n" + url + "\t" + "".join(Breadcrumb_d) + "\t" + title_d + "\t" + option_d + "\t" + price_d + "\t" + sku_d)
                print("End")
                save_details.close()
            except:
                print("Not Found SKU")
        #  =====================================================================================================================
        #     try:
        #         print('*********************** Second Options ************************')
        #         second = Select(driver.find_element(By.XPATH, '//*[@id="CC-prodDetails-sku-VisualSignals_x_lensStyleVariant"]'))
        #         input2 = len(second.options)
        #         time.sleep(3)
        #         for item2 in range(1, input2):
        #             second = Select(driver.find_element(By.XPATH, '//*[@id="CC-prodDetails-sku-VisualSignals_x_lensStyleVariant"]'))
        #             print("second loop = ", item2)
        #             second.select_by_index(item2)        #
        #             time.sleep(3)
        #             driver.get(driver.current_url)
        #             time.sleep(3)
        #
        #             try:
        #                 print("************************************* Price : ****************************************")
        #                 price = driver.find_element(By.ID, 'wi700851-fs-product-list-price-id')
        #                 price_d = price.text
        #                 print("Price = ", price_d)
        #             except:
        #                 price_d = "Not Found"
        #                 print("Not Found Price")
        #             try:
        #                 print("************************************* sku : ****************************************")
        #                 sku = driver.find_element(By.CLASS_NAME, 'cc-sku')
        #                 sku_d = sku.text
        #                 print("sku = ", sku_d)
        #
        #                 # save_details: TextIO = open("main_files.xlsx", "a+", encoding="utf-8")
        #                 # save_details.write("\n" + url + "\t" + "".join(Breadcrumb_d) + "\t" + title_d + "\t" + price_d + "\t" + sku_d)
        #                 # print("End")
        #                 # save_details.close()
        #                 # print("\n ***** Record stored into federal signal  files. *****")
        #             except:
        #                 print("Not Found SKU")
        #     except:
        #             print("Second Options is Not Found")

    except:
        print("Not Found For Loop data")
        # print(e)
    # =================================================================================================================
    try:
        print("************************************* Price : ****************************************")
        price = driver.find_element(By.ID, 'wi700851-fs-product-list-price-id')
        price_d = price.text
        print("Price = ", price_d)
    except:
        price_d = "Not Found"
        print("Not Found Price")

    try:
        print("************************************* sku : ****************************************")
        sku = driver.find_element(By.CLASS_NAME, 'cc-sku')
        sku_d = sku.text
        print("sku = ", sku_d)
    except:
        print("Not Found SKU")

    try:
        print("************************************* Description : ****************************************")
        Description = driver.find_element(By.ID, 'wi700851-fs-product-long-description-id')
        Description_d = Description.text.replace('\n', '')
        print("Description = ", Description_d)
    except:
        print("Not Found")

    try:
        print("************************************* Feature : ****************************************")
        feature = driver.find_element(By.ID, 'Features')
        feature_d = feature.text.replace('\n', '')
        print("feature = ", feature_d)
    except:
        print("Not Found")

    try:
        print("************************************* pdf : ****************************************")
        pdf = driver.find_elements(By.CLASS_NAME, 'link-design ')
        for d in pdf:
            pdf_d = d.get_attribute('href')
            print("Pdf = ", pdf_d)

            save_details: TextIO = open("main_files.xlsx", "a+", encoding="utf-8")
            save_details.write("\n" + url + "\t" + "".join(Breadcrumb_d) + "\t" + title_d + "\t" + option_d + "\t" + price_d + "\t" + sku_d + "\t" + Description_d + "\t" + feature_d + "\t" + pdf_d)
            print("End")
            save_details.close()
            print("\n ***** Record stored into pdf  files. *****")
    except:
        print("Not Found")

    try:
        print("************************************* Images : ****************************************")
        image = driver.find_element(By.ID, 'cc_img__resize_wrapper').find_elements(By.TAG_NAME, 'img')
        for imgs in image:
            image_d = imgs.get_attribute('src')
            print("image_d = ", image_d)

            save_details: TextIO = open("main_files.xlsx", "a+", encoding="utf-8")
            save_details.write("\n" + url + "\t" + "".join(Breadcrumb_d) + "\t" + title_d + "\t" + option_d + "\t" + price_d + "\t" + sku_d + "\t" + Description_d + "\t" + feature_d + "\t" + pdf_d + "\t" + image_d)
            print("End")
            save_details.close()
            print("\n ***** Record stored into Images  files. *****")
    except:
        print("Not Found")



#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#AIDES:
#https://www.raspberrypi.org/forums/viewtopic.php?t=210680


#!/usr/bin/python3
import serial
import pynmea2

ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
reader = pynmea2.NMEAStreamReader()

def decodeGGA(GGAobj):
    print ("GGA TS:", GGAobj.timestamp)
    print ("GGA Lat:", GGAobj.lat)
    print ("GGA Lat Dir:", GGAobj.lat_dir)
    print ("GGA Lon:", GGAobj.lon)
    print ("GGA Lon Dir:", GGAobj.lon_dir)
    print ("GGA QI:", GGAobj.gps_qual)
    print ("GGA num sats:", GGAobj.num_sats)
    print ("GGA horiz dilution:", GGAobj.horizontal_dil)
    print ("GGA Alt amsl:", GGAobj.altitude)
    print ("GGA Alt units:", GGAobj.altitude_units)
    print ("GGA Geoidal Sep:", GGAobj.geo_sep)
    print ("GGA Geoidal Sep units:", GGAobj.geo_sep_units)
    if (GGAobj.age_gps_data): print ("GGA Age GPS data:", GGAobj.age_gps_data)
    if (GGAobj.ref_station_id): print ("GGA ref station ID:", GGAobj.ref_station_id)

def msg_num_pad(msg_num, idx):
    return str(((int(msg_num) - 1) * 4) + idx).zfill(2)+":"

def decodeGSV(GSVobj):
#http://aprs.gids.nl/nmea/#gsv
    #print ("GSV msg_num", GSVobj.msg_num)
    sat_num = []
    for i in range(1,5):
        sat_num.append(msg_num_pad(GSVobj.msg_num,i))
    if int(GSVobj.msg_num) == 1:
        print ("GSV Sats in view", GSVobj.num_sv_in_view)
    print ("GSV", sat_num[0], GSVobj.sv_prn_num_1, sat_num[1], GSVobj.sv_prn_num_2, sat_num[2], GSVobj.sv_prn_num_3, sat_num[3], GSVobj.sv_prn_num_4)

def decodeTXT(TXTobj):
    #print ("TXT msg_num", TXTobj.msg_num)
    #print ("TXT msg_type", TXTobj.msg_type)
    print ("TXT", TXTobj.text)

def decodeGLL(GLLobj):
    print ("GLL TS:", GLLobj.timestamp)
    print ("GLL Lat:", GLLobj.lat)
    print ("GLL Lon:", GLLobj.lon)
    print ("GLL Status:", GLLobj.status)
    print ("GLL FAA mode:", GLLobj.faa_mode)

def decodeRMC(RMCobj):
    print ("RMC TS:", RMCobj.timestamp)
    print ("RMC status:", RMCobj.status)
    print ("RMC lat:", RMCobj.lat)
    print ("RMC lon:", RMCobj.lon)
    print ("RMC speed:", RMCobj.spd_over_grnd)
    print ("RMC date:", RMCobj.datestamp)
    if (RMCobj.mag_variation): print ("RMC Mag var:", RMCobj.mag_variation)
    if (RMCobj.mag_variation): print ("RMC Mag var dir:", RMCobj.mag_var_dir)

def decodeVTG(VTGobj):
    if (VTGobj.true_track): print ("VTG true track:", VTGobj.true_track)
    if (VTGobj.true_track): print ("VTG true track sym:", VTGobj.true_track_sym)
    if (VTGobj.mag_track): print ("VTG mag track:", VTGobj.mag_track)
    if (VTGobj.mag_track): print ("VTG mag track sym:", VTGobj.mag_track_sym)
    print ("VTG speed Kts:", VTGobj.spd_over_grnd_kts)
    print ("VTG speed Kts sym:", VTGobj.spd_over_grnd_kts_sym)
    print ("VTG speed Km/h:", VTGobj.spd_over_grnd_kmph)
    print ("VTG speed Km/h sym:", VTGobj.spd_over_grnd_kmph_sym)
    print ("VTG FAA mode:", VTGobj.faa_mode)

def decodeGSA(GSAobj):
    print ("GSA mode:", GSAobj.mode)
    print ("GSA mode fix type:", GSAobj.mode_fix_type)
    if (GSAobj.sv_id01): print ("GSA SV_O1:", GSAobj.sv_id01)
    if (GSAobj.sv_id02): print ("GSA SV 02:", GSAobj.sv_id02)
    if (GSAobj.sv_id03): print ("GSA SV 03:", GSAobj.sv_id03)
    if (GSAobj.sv_id04): print ("GSA SV 04:", GSAobj.sv_id04)
    if (GSAobj.sv_id05): print ("GSA SV 05:", GSAobj.sv_id05)
    if (GSAobj.sv_id06): print ("GSA SV 06:", GSAobj.sv_id06)
    if (GSAobj.sv_id07): print ("GSA SV 07:", GSAobj.sv_id07)
    if (GSAobj.sv_id08): print ("GSA SV 08:", GSAobj.sv_id08)
    if (GSAobj.sv_id09): print ("GSA SV 09:", GSAobj.sv_id09)
    if (GSAobj.sv_id10): print ("GSA SV 10:", GSAobj.sv_id10)
    if (GSAobj.sv_id11): print ("GSA SV 11:", GSAobj.sv_id11)
    if (GSAobj.sv_id12): print ("GSA SV 12:", GSAobj.sv_id12)

while True:
    data = ser.read(16).decode('utf-8')
    for msg in reader.next(data):
        #print(msg)
        parsed = pynmea2.parse(str(msg))
        if parsed.sentence_type == "GGA":
            decodeGGA(parsed)
        elif parsed.sentence_type == "GSV":
            decodeGSV(parsed)
        elif parsed.sentence_type == "TXT":
            decodeTXT(parsed)
        elif parsed.sentence_type == "GLL":
            decodeGLL(parsed)
        elif parsed.sentence_type == "RMC":
            decodeRMC(parsed)
        elif parsed.sentence_type == "VTG":
            decodeVTG(parsed)
        elif parsed.sentence_type == "GSA":
            decodeGSA(parsed)
        else:
            print (parsed.sentence_type)

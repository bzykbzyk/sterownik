#===============================================================================
#                         Parametry wspólne
#
# Tutaj wpisz parametry globalne pracy
#===============================================================================
#======== parametry CO ===============

tempZadanaGora = 50.2;
tempZadanaDol = 50;

#======== parametry podtrzymania ===============

podtrzymanie_postoj = 10 # w minutach
podtrzymanie_podajnik = 10
podtrzymanie_przerwa = 30
podtrzymanie_nadmuch = 38

#======== paramtery autoregulacji spalin
tspalin = 100
deltaspalin = 10
max_obr_dmuchawy = 52
tryb_autodopalania = False
opoznienie = 3

#======== Korekta grupowa =============

czasPodawania = 0;
czasPrzerwy   = 0;
czasNawiewu   = 0;
mocNawiewu    = 0;

#========== Parametry bloków ===================================================
# możliwe tryby to - start, stop, normal, oba, jeden_start, jeden_normal, jeden_stop

czas_podawania = [ 5 ,  0,  0,  3,  0,  0]
czas_przerwy   = [ 20, 30, 60, 13, 20,100]
czas_nawiewu   = [ 20, 30, 60, 13, 20,100]
moc_nawiewu    = [ 46, 43, 40, 43, 40, 40]
tryb = ['start','start','jeden_normal','normal','normal','stop']

#=========== Parametry trybu Lato ==============================================

Tryb_autolato = False
T_zewnetrzna_lato = 15;
T_dolna_CWU = 44;


TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#==================================================
# build a support library

LIBRARY_IOC += astlib

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxxRecord
# install astlib.dbd into <top>/dbd
#DBD += astlib.dbd

# specify all source files to be compiled and added to the library
#astlib_SRCS += xxx
SRCS.c    = $(wildcard ../*.c)
astlib_SRCS += $(strip $(patsubst ../%.c,    %.o, $(SRCS.c)))

LIB_LIBS += slalib
LIB_LIBS += timelib

INC += astLib.h
INC += astsys.h

astlib_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE


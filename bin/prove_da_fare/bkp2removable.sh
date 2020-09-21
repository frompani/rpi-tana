#!/bin/bash
#script per fare il backup dei dati sul raid del server .180 sul disco esterno
rsync -avz  fabrizio@192.168.10.180:/raid /media/removable/

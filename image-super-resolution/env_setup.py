from PIL import Image
from ISR.models import RDN, RRDN

# trigger a download of the models
rdn = RDN(weights='psnr-small')
rdn = RDN(weights='psnr-large')
rdn = RDN(weights='noise-cancel')
rrdn = RRDN(weights='gans')
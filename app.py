{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import pytesseract"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "img =cv2.imread('img.jpg')\n",
    "\n",
    "\n",
    "img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)\n",
    "imgresize=cv2.resize(img1,(1000,900))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "pytesseract.pytesseract.tesseract_cmd='C:\\\\Program Files\\\\Tesseract-OCR\\\\tesseract.exe'\n",
    "boxes = pytesseract.image_to_data(imgresize)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#To make rectangle\n",
    "\n",
    "for b in boxes.splitlines():\n",
    "    b=b.split()\n",
    "    if b[-1] == '(adhaary':\n",
    "        x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])\n",
    "        #print(x,y,w,h)\n",
    "        cv2.rectangle(imgresize, (42+w+x,y+h),(x+400,y-5),(255,0,0),cv2.FILLED)\n",
    "        cv2.imshow(\"reeedfgf\",imgresize)\n",
    "        if cv2.waitKey(0)==27:\n",
    "            pass\n",
    "    cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "for b in boxes.splitlines():\n",
    "    b=b.split()\n",
    "    #print(b)\n",
    "    if b[7] == '645' and b[8] == '157':\n",
    "        x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])\n",
    "        #rint(x,y,w,h)\n",
    "        cv2.rectangle(imgresize,(x,y),(w+x,y+h),(255,0,0),1)\n",
    "        cv2.imshow(\"reeedfgf\",imgresize)\n",
    "        if cv2.waitKey(0)==27:\n",
    "            pass\n",
    "    cv2.destroyAllWindows()\n",
    "        \n",
    "\n",
    "         \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "    cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

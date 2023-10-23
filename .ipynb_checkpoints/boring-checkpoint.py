{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1db4f75c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "87\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "regex = re.compile(r'\\d*$')\n",
    "mo = regex.search('My number is 87')\n",
    "print(mo.group())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3374f554",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

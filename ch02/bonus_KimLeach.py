{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "905610b3-85be-425a-b002-b250d0c13bfe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.7"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Student Data - Kim Leach - Min GPA\n",
    "GPA = (4.0, 3.95, 2.3, 4.0, 1.7, 3.6, 2.73, 3.71)\n",
    "min(GPA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c1876458-d62f-4739-85f1-7b8bf87694ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.0"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Max GPA\n",
    "max(GPA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d6064eff-1993-4dfd-afcf-064902411e55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.0"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(GPA)//len(GPA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "02b5244e-4890-4b4b-a4d7-547f75ff83ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(263085, 220611, 408531), (223166, 322124, 322170), (216926, 321047, 241992), (240355, 215050, 220396)]\n"
     ]
    }
   ],
   "source": [
    "#grouping students\n",
    "stu_list = (263085,220611,408531,223166,322124,322170,216926,321047,241992,240355,215050,220396)\n",
    "split_students = [stu_list[x:x+3] for x in range(0, len(stu_list), 3)]\n",
    "print(split_students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed08c751-bc1d-4c82-ad91-1ef3044b4a05",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

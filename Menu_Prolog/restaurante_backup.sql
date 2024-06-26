PGDMP  '    2            
    {            restaurante    16.0    16.0 G               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    24576    restaurante    DATABASE     �   CREATE DATABASE restaurante WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Costa Rica.1252';
    DROP DATABASE restaurante;
                postgres    false                        2615    24587    ingrediente    SCHEMA        CREATE SCHEMA ingrediente;
    DROP SCHEMA ingrediente;
                postgres    false                        2615    24724    menu    SCHEMA        CREATE SCHEMA menu;
    DROP SCHEMA menu;
                postgres    false                        2615    33148    pago    SCHEMA        CREATE SCHEMA pago;
    DROP SCHEMA pago;
                postgres    false            �            1259    24692    general    TABLE     "  CREATE TABLE ingrediente.general (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    calorias numeric,
    naturaleza_dietetica character varying(15),
    sabor character varying(20),
    precio numeric,
    desayuno boolean,
    almuerzo boolean,
    cena boolean
);
     DROP TABLE ingrediente.general;
       ingrediente         heap    postgres    false    6            �            1259    24700    bebida    TABLE     �   CREATE TABLE ingrediente.bebida (
    categoria character varying(20),
    temperatura character varying(20),
    base character varying(20)
)
INHERITS (ingrediente.general);
    DROP TABLE ingrediente.bebida;
       ingrediente         heap    postgres    false    221    6            �            1259    24691    general_id_ingrediente_seq    SEQUENCE     �   CREATE SEQUENCE ingrediente.general_id_ingrediente_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE ingrediente.general_id_ingrediente_seq;
       ingrediente          postgres    false    6    221                       0    0    general_id_ingrediente_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE ingrediente.general_id_ingrediente_seq OWNED BY ingrediente.general.id;
          ingrediente          postgres    false    220            �            1259    24712 
   guarnicion    TABLE     �   CREATE TABLE ingrediente.guarnicion (
    categoria character varying(20),
    tamano character varying(20),
    metodo_coccion character varying(20)
)
INHERITS (ingrediente.general);
 #   DROP TABLE ingrediente.guarnicion;
       ingrediente         heap    postgres    false    221    6            �            1259    24718    postre    TABLE     �   CREATE TABLE ingrediente.postre (
    textura character varying(20),
    temperatura character varying(20)
)
INHERITS (ingrediente.general);
    DROP TABLE ingrediente.postre;
       ingrediente         heap    postgres    false    221    6            �            1259    24706    proteina    TABLE     �   CREATE TABLE ingrediente.proteina (
    origen character varying(20),
    textura character varying(20),
    metodo_coccion character varying(20)
)
INHERITS (ingrediente.general);
 !   DROP TABLE ingrediente.proteina;
       ingrediente         heap    postgres    false    221    6            �            1259    24726    menu    TABLE     r   CREATE TABLE menu.menu (
    id integer NOT NULL,
    calorias numeric DEFAULT 0,
    precio numeric DEFAULT 0
);
    DROP TABLE menu.menu;
       menu         heap    postgres    false    7            �            1259    24736    plato    TABLE     �   CREATE TABLE menu.plato (
    proteina integer DEFAULT 0 NOT NULL,
    guarnicion_1 integer DEFAULT 0 NOT NULL,
    guarnicion_2 integer DEFAULT 0 NOT NULL,
    guarnicion_3 integer DEFAULT 0 NOT NULL
)
INHERITS (menu.menu);
    DROP TABLE menu.plato;
       menu         heap    postgres    false    227    7            �            1259    32916    combo    TABLE     l   CREATE TABLE menu.combo (
    bebida integer NOT NULL,
    postre integer NOT NULL
)
INHERITS (menu.plato);
    DROP TABLE menu.combo;
       menu         heap    postgres    false    228    7            �            1259    24725    menu_id_seq    SEQUENCE     �   CREATE SEQUENCE menu.menu_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
     DROP SEQUENCE menu.menu_id_seq;
       menu          postgres    false    7    227                       0    0    menu_id_seq    SEQUENCE OWNED BY     7   ALTER SEQUENCE menu.menu_id_seq OWNED BY menu.menu.id;
          menu          postgres    false    226            �            1259    33150    factura    TABLE     �   CREATE TABLE pago.factura (
    id integer NOT NULL,
    cliente character varying(100) NOT NULL,
    descripcion character varying(1000) NOT NULL,
    total numeric NOT NULL,
    tipo character varying NOT NULL
);
    DROP TABLE pago.factura;
       pago         heap    postgres    false    8            �            1259    33149    factura_id_seq    SEQUENCE     �   CREATE SEQUENCE pago.factura_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE pago.factura_id_seq;
       pago          postgres    false    8    231                       0    0    factura_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE pago.factura_id_seq OWNED BY pago.factura.id;
          pago          postgres    false    230            �            1259    24578    comida    TABLE     �   CREATE TABLE public.comida (
    id integer NOT NULL,
    ingrediente1 character varying,
    ingrediente2 character varying,
    ingrediente3 character varying
);
    DROP TABLE public.comida;
       public         heap    postgres    false            �            1259    24577    comida_id_seq    SEQUENCE     �   CREATE SEQUENCE public.comida_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.comida_id_seq;
       public          postgres    false    219                       0    0    comida_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.comida_id_seq OWNED BY public.comida.id;
          public          postgres    false    218            F           2604    24703 	   bebida id    DEFAULT     }   ALTER TABLE ONLY ingrediente.bebida ALTER COLUMN id SET DEFAULT nextval('ingrediente.general_id_ingrediente_seq'::regclass);
 =   ALTER TABLE ingrediente.bebida ALTER COLUMN id DROP DEFAULT;
       ingrediente          postgres    false    220    222            E           2604    24695 
   general id    DEFAULT     ~   ALTER TABLE ONLY ingrediente.general ALTER COLUMN id SET DEFAULT nextval('ingrediente.general_id_ingrediente_seq'::regclass);
 >   ALTER TABLE ingrediente.general ALTER COLUMN id DROP DEFAULT;
       ingrediente          postgres    false    220    221    221            H           2604    24715    guarnicion id    DEFAULT     �   ALTER TABLE ONLY ingrediente.guarnicion ALTER COLUMN id SET DEFAULT nextval('ingrediente.general_id_ingrediente_seq'::regclass);
 A   ALTER TABLE ingrediente.guarnicion ALTER COLUMN id DROP DEFAULT;
       ingrediente          postgres    false    220    224            I           2604    24721 	   postre id    DEFAULT     }   ALTER TABLE ONLY ingrediente.postre ALTER COLUMN id SET DEFAULT nextval('ingrediente.general_id_ingrediente_seq'::regclass);
 =   ALTER TABLE ingrediente.postre ALTER COLUMN id DROP DEFAULT;
       ingrediente          postgres    false    220    225            G           2604    24709    proteina id    DEFAULT        ALTER TABLE ONLY ingrediente.proteina ALTER COLUMN id SET DEFAULT nextval('ingrediente.general_id_ingrediente_seq'::regclass);
 ?   ALTER TABLE ingrediente.proteina ALTER COLUMN id DROP DEFAULT;
       ingrediente          postgres    false    223    220            T           2604    32919    combo id    DEFAULT     _   ALTER TABLE ONLY menu.combo ALTER COLUMN id SET DEFAULT nextval('menu.menu_id_seq'::regclass);
 5   ALTER TABLE menu.combo ALTER COLUMN id DROP DEFAULT;
       menu          postgres    false    226    229            U           2604    32920    combo calorias    DEFAULT     A   ALTER TABLE ONLY menu.combo ALTER COLUMN calorias SET DEFAULT 0;
 ;   ALTER TABLE menu.combo ALTER COLUMN calorias DROP DEFAULT;
       menu          postgres    false    229            V           2604    32921    combo precio    DEFAULT     ?   ALTER TABLE ONLY menu.combo ALTER COLUMN precio SET DEFAULT 0;
 9   ALTER TABLE menu.combo ALTER COLUMN precio DROP DEFAULT;
       menu          postgres    false    229            W           2604    32922    combo proteina    DEFAULT     A   ALTER TABLE ONLY menu.combo ALTER COLUMN proteina SET DEFAULT 0;
 ;   ALTER TABLE menu.combo ALTER COLUMN proteina DROP DEFAULT;
       menu          postgres    false    229            X           2604    32923    combo guarnicion_1    DEFAULT     E   ALTER TABLE ONLY menu.combo ALTER COLUMN guarnicion_1 SET DEFAULT 0;
 ?   ALTER TABLE menu.combo ALTER COLUMN guarnicion_1 DROP DEFAULT;
       menu          postgres    false    229            Y           2604    32924    combo guarnicion_2    DEFAULT     E   ALTER TABLE ONLY menu.combo ALTER COLUMN guarnicion_2 SET DEFAULT 0;
 ?   ALTER TABLE menu.combo ALTER COLUMN guarnicion_2 DROP DEFAULT;
       menu          postgres    false    229            Z           2604    32925    combo guarnicion_3    DEFAULT     E   ALTER TABLE ONLY menu.combo ALTER COLUMN guarnicion_3 SET DEFAULT 0;
 ?   ALTER TABLE menu.combo ALTER COLUMN guarnicion_3 DROP DEFAULT;
       menu          postgres    false    229            J           2604    24729    menu id    DEFAULT     ^   ALTER TABLE ONLY menu.menu ALTER COLUMN id SET DEFAULT nextval('menu.menu_id_seq'::regclass);
 4   ALTER TABLE menu.menu ALTER COLUMN id DROP DEFAULT;
       menu          postgres    false    227    226    227            M           2604    24739    plato id    DEFAULT     _   ALTER TABLE ONLY menu.plato ALTER COLUMN id SET DEFAULT nextval('menu.menu_id_seq'::regclass);
 5   ALTER TABLE menu.plato ALTER COLUMN id DROP DEFAULT;
       menu          postgres    false    228    226            N           2604    24740    plato calorias    DEFAULT     A   ALTER TABLE ONLY menu.plato ALTER COLUMN calorias SET DEFAULT 0;
 ;   ALTER TABLE menu.plato ALTER COLUMN calorias DROP DEFAULT;
       menu          postgres    false    228            O           2604    24741    plato precio    DEFAULT     ?   ALTER TABLE ONLY menu.plato ALTER COLUMN precio SET DEFAULT 0;
 9   ALTER TABLE menu.plato ALTER COLUMN precio DROP DEFAULT;
       menu          postgres    false    228            [           2604    33153 
   factura id    DEFAULT     d   ALTER TABLE ONLY pago.factura ALTER COLUMN id SET DEFAULT nextval('pago.factura_id_seq'::regclass);
 7   ALTER TABLE pago.factura ALTER COLUMN id DROP DEFAULT;
       pago          postgres    false    230    231    231            D           2604    24581 	   comida id    DEFAULT     f   ALTER TABLE ONLY public.comida ALTER COLUMN id SET DEFAULT nextval('public.comida_id_seq'::regclass);
 8   ALTER TABLE public.comida ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    219    219                      0    24700    bebida 
   TABLE DATA           �   COPY ingrediente.bebida (id, nombre, calorias, naturaleza_dietetica, sabor, precio, desayuno, almuerzo, cena, categoria, temperatura, base) FROM stdin;
    ingrediente          postgres    false    222   �O                 0    24692    general 
   TABLE DATA           {   COPY ingrediente.general (id, nombre, calorias, naturaleza_dietetica, sabor, precio, desayuno, almuerzo, cena) FROM stdin;
    ingrediente          postgres    false    221   R       	          0    24712 
   guarnicion 
   TABLE DATA           �   COPY ingrediente.guarnicion (id, nombre, calorias, naturaleza_dietetica, sabor, precio, desayuno, almuerzo, cena, categoria, tamano, metodo_coccion) FROM stdin;
    ingrediente          postgres    false    224   $R       
          0    24718    postre 
   TABLE DATA           �   COPY ingrediente.postre (id, nombre, calorias, naturaleza_dietetica, sabor, precio, desayuno, almuerzo, cena, textura, temperatura) FROM stdin;
    ingrediente          postgres    false    225   �T                 0    24706    proteina 
   TABLE DATA           �   COPY ingrediente.proteina (id, nombre, calorias, naturaleza_dietetica, sabor, precio, desayuno, almuerzo, cena, origen, textura, metodo_coccion) FROM stdin;
    ingrediente          postgres    false    223   �V                 0    32916    combo 
   TABLE DATA           w   COPY menu.combo (id, calorias, precio, proteina, guarnicion_1, guarnicion_2, guarnicion_3, bebida, postre) FROM stdin;
    menu          postgres    false    229   �X                 0    24726    menu 
   TABLE DATA           2   COPY menu.menu (id, calorias, precio) FROM stdin;
    menu          postgres    false    227   6Y                 0    24736    plato 
   TABLE DATA           g   COPY menu.plato (id, calorias, precio, proteina, guarnicion_1, guarnicion_2, guarnicion_3) FROM stdin;
    menu          postgres    false    228   SY                 0    33150    factura 
   TABLE DATA           F   COPY pago.factura (id, cliente, descripcion, total, tipo) FROM stdin;
    pago          postgres    false    231   �Y                 0    24578    comida 
   TABLE DATA           N   COPY public.comida (id, ingrediente1, ingrediente2, ingrediente3) FROM stdin;
    public          postgres    false    219   �Y                  0    0    general_id_ingrediente_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('ingrediente.general_id_ingrediente_seq', 105, true);
          ingrediente          postgres    false    220                       0    0    menu_id_seq    SEQUENCE SET     8   SELECT pg_catalog.setval('menu.menu_id_seq', 11, true);
          menu          postgres    false    226                       0    0    factura_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('pago.factura_id_seq', 1, false);
          pago          postgres    false    230                       0    0    comida_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.comida_id_seq', 1, true);
          public          postgres    false    218            a           2606    24773    bebida bebida_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY ingrediente.bebida
    ADD CONSTRAINT bebida_pkey PRIMARY KEY (id);
 A   ALTER TABLE ONLY ingrediente.bebida DROP CONSTRAINT bebida_pkey;
       ingrediente            postgres    false    222            _           2606    24699    general general_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY ingrediente.general
    ADD CONSTRAINT general_pkey PRIMARY KEY (id);
 C   ALTER TABLE ONLY ingrediente.general DROP CONSTRAINT general_pkey;
       ingrediente            postgres    false    221            e           2606    24771    guarnicion guarnicion_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY ingrediente.guarnicion
    ADD CONSTRAINT guarnicion_pkey PRIMARY KEY (id);
 I   ALTER TABLE ONLY ingrediente.guarnicion DROP CONSTRAINT guarnicion_pkey;
       ingrediente            postgres    false    224            g           2606    24769    postre postre_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY ingrediente.postre
    ADD CONSTRAINT postre_pkey PRIMARY KEY (id);
 A   ALTER TABLE ONLY ingrediente.postre DROP CONSTRAINT postre_pkey;
       ingrediente            postgres    false    225            c           2606    24767    proteina proteina_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY ingrediente.proteina
    ADD CONSTRAINT proteina_pkey PRIMARY KEY (id);
 E   ALTER TABLE ONLY ingrediente.proteina DROP CONSTRAINT proteina_pkey;
       ingrediente            postgres    false    223            m           2606    32929    combo combo_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY menu.combo
    ADD CONSTRAINT combo_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY menu.combo DROP CONSTRAINT combo_pkey;
       menu            postgres    false    229            i           2606    24735    menu menu_pkey 
   CONSTRAINT     J   ALTER TABLE ONLY menu.menu
    ADD CONSTRAINT menu_pkey PRIMARY KEY (id);
 6   ALTER TABLE ONLY menu.menu DROP CONSTRAINT menu_pkey;
       menu            postgres    false    227            k           2606    24777    plato plato_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY menu.plato
    ADD CONSTRAINT plato_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY menu.plato DROP CONSTRAINT plato_pkey;
       menu            postgres    false    228            o           2606    33157    factura factura_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY pago.factura
    ADD CONSTRAINT factura_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY pago.factura DROP CONSTRAINT factura_pkey;
       pago            postgres    false    231            ]           2606    24585    comida comida_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.comida
    ADD CONSTRAINT comida_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.comida DROP CONSTRAINT comida_pkey;
       public            postgres    false    219            p           2606    24874    plato plato_guarnicion_1_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY menu.plato
    ADD CONSTRAINT plato_guarnicion_1_fkey FOREIGN KEY (guarnicion_1) REFERENCES ingrediente.guarnicion(id) NOT VALID;
 E   ALTER TABLE ONLY menu.plato DROP CONSTRAINT plato_guarnicion_1_fkey;
       menu          postgres    false    224    228    4709            q           2606    24879    plato plato_guarnicion_2_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY menu.plato
    ADD CONSTRAINT plato_guarnicion_2_fkey FOREIGN KEY (guarnicion_2) REFERENCES ingrediente.guarnicion(id) NOT VALID;
 E   ALTER TABLE ONLY menu.plato DROP CONSTRAINT plato_guarnicion_2_fkey;
       menu          postgres    false    4709    224    228            r           2606    24884    plato plato_guarnicion_3_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY menu.plato
    ADD CONSTRAINT plato_guarnicion_3_fkey FOREIGN KEY (guarnicion_3) REFERENCES ingrediente.guarnicion(id) NOT VALID;
 E   ALTER TABLE ONLY menu.plato DROP CONSTRAINT plato_guarnicion_3_fkey;
       menu          postgres    false    228    224    4709            s           2606    24869    plato plato_proteina_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY menu.plato
    ADD CONSTRAINT plato_proteina_fkey FOREIGN KEY (proteina) REFERENCES ingrediente.proteina(id) NOT VALID;
 A   ALTER TABLE ONLY menu.plato DROP CONSTRAINT plato_proteina_fkey;
       menu          postgres    false    223    228    4707               $  x��T;��0��N�"-�S�:� ��Ell��Y��\ȤAS.��()S��#�b!%YҒ�&p��3of�<&����2^X��ሪ�@f	�����RX�����`�T�BIH(�Et�%gB���-?J�������̂ݹO�6v/\�Ps��@^%x:h���#����~O5+Ì���4���z_�2e����xDm�L�h�#�4�0�",G���*����d���9 ���K���i��v�o��nk�7K3^9S3�z�?!�SvEK���s/�1�g`q�`/�/K�&�^��a뷡�,�[U4TGW;}����4Zª3c�s�M����U���xf�8I��a�M�a���{d��t0%���w�-�m�݂�D/EJ�;˕ɠI�2���/���%?��b�;G2�wW��P�!����
W�*I,й�y�N?8Ne���KrL����Qhn4y��d�vG)��?�r*�_���c�'�k���zA�����u/Y;v1}�Np"��} �����G� �[�c�_�r�K            x������ � �      	   O  x������@���S�	���#�DQ."�S�S�a���e�̲W�6)S\�K�ˬ���D.\����|��:0�_.�F�o�dm"%�Q��B��`U]~,Ixm�NNoY�	�<a#��XX/Ь�w����~�������
5�Dv�5���w��_Qph�uH�ָ�1�'2�R��!;��n}�H�p{}I'ة#O��`��e��\��%#1Ԕ�����*F?��t��Β���(ʲ��b�SB��	Bݳ�r��$�\=:&� ?��X���*����Y��B���q0d���B��ͭ�.6܏u���0>��|^�2�om����I��Z���l��w��,)�h��ɊL�ة	�Ϋ�.���5��q8H�����kU���$�_V�`��Xɣ�?nuLj��������+�����`p�b^�@��
�0�ȋFT��%EU��{�Q�Z�y|/51���i�í[�?�pj�Rzɂl ,�N������a�Hj-�=�?��Mf��?)����#�;�&��!)�a�q�xm4�4`Wnץ�#]�.Y/�\V�Ҙ���ːe�]U����W��k+���YF�      
     x��T=n�0��O�%Y�ZIt��,=;D)2%%�֣� ��u����8q,��A��O���9ܣk1�)�le5�i��Q�M�+�|C;�>wx$�W;eEIcm��QZ#$��Nзn KآoI�#� f�,�,ac;�钵��Ζ�-c~v-��L���w� ῿�͙�+��sx�&p�z[eFôj�?��U�� B�����0���9S���{ez�A�4� Č�$#3X?y���#��� C.�r�(�������j4c�X�v�rZ������m�ʲ���� �_�N4� �}w^Z�>`N��ٽj�YM>��<�D���Q�*�E=F�i�v�6�~�Fs���M���k��)|⪲7�Y��D��\��y�d���u���6dTۮ�Gڏh���w[r�w2:*c����J��� l�Vd�)Xt�w}zuQʳf^2�c�B�y\�jMÚ�#�`��S�p	6h���3�}���i��$�|"H/V/C6֘y�x9A������5E$�$�7��.��?}��%           x���ώ�0���S�pܦZ�Е�&�^f�7q������[����/��O�qZE"Ɵg~�al?����Z)q�M-9�V֫����Cv�<5�.`kx�J��ShP�>���"G��j��wOF��Y���I6������)'�op�F	/�QzV��Y��2oI�Euه*�h�T
!.jɖk�b���w�pa(�%�J�*F�M���/�ԢWa�top�Ga͏,]��y�$	�}��*y�f�&_�1[`��oF�$���X���k����!�6GK~�hS	Ct�^�Ѥ��z@���ꓞ���^�$�P��?2L/�(�����H}�p-q\]N��Vq;\�Ye�E��'���#q�/f^i<�Q����������*.��#����3���lwp��NQ��N��).��
gn�	p��+�'<XI;��t�(M�eL*�֘���.u+��_D������=/�	q��U�@�
�#���g�<��QyE�d�)�O��o.�Su�`��	1��N�p���gҠ���*��~y9         H   x�ɱ�@D��S�@a�^�=�I�ْ/b<ɢ.��ede��g]tb�"М��C���H&�q3{��             x������ � �         K   x�%���0�3�3(&ݥ���$�p���Ly`�.(�B�e�����t����l�W�	3�ZH^�#^7�]�            x������ � �         !   x�3�,�����,H,H,�,N�)N����� h�N     
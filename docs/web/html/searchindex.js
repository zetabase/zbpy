Search.setIndex({docnames:["index","modules","zbpy"],envversion:53,filenames:["index.rst","modules.rst","zbpy.rst"],objects:{"":{zbpy:[2,0,0,"-"]},"zbpy.auth":{make_credential_ecdsa:[2,1,1,""],make_credential_jwt:[2,1,1,""]},"zbpy.basicqueries":{QueryAnd:[2,2,1,""],QueryEquals:[2,2,1,""],QueryGreaterThan:[2,2,1,""],QueryGreaterThanEqual:[2,2,1,""],QueryLessThan:[2,2,1,""],QueryLessThanEqual:[2,2,1,""],QueryNotEqual:[2,2,1,""],QueryOr:[2,2,1,""],QueryTextSearch:[2,2,1,""],query_object_typify:[2,1,1,""]},"zbpy.basicqueries.QueryAnd":{to_sub_query:[2,3,1,""]},"zbpy.basicqueries.QueryEquals":{to_sub_query:[2,3,1,""]},"zbpy.basicqueries.QueryGreaterThan":{to_sub_query:[2,3,1,""]},"zbpy.basicqueries.QueryGreaterThanEqual":{to_sub_query:[2,3,1,""]},"zbpy.basicqueries.QueryLessThan":{to_sub_query:[2,3,1,""]},"zbpy.basicqueries.QueryLessThanEqual":{to_sub_query:[2,3,1,""]},"zbpy.basicqueries.QueryNotEqual":{to_sub_query:[2,3,1,""]},"zbpy.basicqueries.QueryOr":{to_sub_query:[2,3,1,""]},"zbpy.basicqueries.QueryTextSearch":{to_sub_query:[2,3,1,""]},"zbpy.cleanqueries":{AndExpression:[2,2,1,""],Expression:[2,2,1,""],Field:[2,2,1,""],OrExpression:[2,2,1,""]},"zbpy.cleanqueries.AndExpression":{to_sub_query:[2,3,1,""]},"zbpy.cleanqueries.Expression":{to_sub_query:[2,3,1,""]},"zbpy.cleanqueries.OrExpression":{to_sub_query:[2,3,1,""]},"zbpy.client":{NewAccount:[2,2,1,""],ZetabaseClient:[2,2,1,""],import_key:[2,1,1,""]},"zbpy.client.NewAccount":{createaccount:[2,3,1,""],magics:[2,4,1,""],registered:[2,4,1,""]},"zbpy.client.ZetabaseClient":{add_permission:[2,3,1,""],auth_login_jwt:[2,3,1,""],check_ready:[2,3,1,""],check_version:[2,3,1,""],confirm_new_sub_user:[2,3,1,""],confirm_user_identity:[2,3,1,""],connect:[2,3,1,""],create_table:[2,3,1,""],delete_key:[2,3,1,""],delete_table:[2,3,1,""],ecdsa_credential:[2,3,1,""],get:[2,3,1,""],get_credential:[2,3,1,""],get_sub_identities:[2,3,1,""],grpc_stub:[2,3,1,""],id:[2,3,1,""],jwt_credential:[2,3,1,""],list_keys:[2,3,1,""],list_tables:[2,3,1,""],new_sub_user:[2,3,1,""],put_data:[2,3,1,""],put_dataframe:[2,3,1,""],put_dataframe_new_table:[2,3,1,""],put_multi:[2,3,1,""],put_np_array:[2,3,1,""],query:[2,3,1,""],set_cert_verify:[2,3,1,""],set_id_key:[2,3,1,""],set_id_password:[2,3,1,""],set_insecure:[2,3,1,""],set_parent:[2,3,1,""],set_server_addr:[2,3,1,""]},"zbpy.cryptography":{encode_private_key:[2,1,1,""],encode_public_key:[2,1,1,""],generate_key_pair:[2,1,1,""],make_zetabase_signature:[2,1,1,""],multi_put_extra_signing_bytes:[2,1,1,""],permission_set_signing_bytes:[2,1,1,""],permission_signing_bytes:[2,1,1,""],permissions_entry_signing_bytes:[2,1,1,""],sign_message_bytes:[2,1,1,""],signing_bytes:[2,1,1,""],table_create_signing_bytes:[2,1,1,""],table_put_extra_signing_bytes:[2,1,1,""],validate_signature_bytes:[2,1,1,""]},"zbpy.datasci":{df_to_kvp:[2,1,1,""],parse_df_column:[2,1,1,""],parse_df_columns:[2,1,1,""],parse_np_array:[2,1,1,""]},"zbpy.indexedfieldentity":{IndexedField:[2,2,1,""],indexed_fields_to_protocol:[2,1,1,""]},"zbpy.indexedfieldentity.IndexedField":{set_language_code:[2,3,1,""],to_protocol:[2,3,1,""]},"zbpy.pagination":{PaginationHandler:[2,2,1,""],standard_pagination_handler:[2,1,1,""]},"zbpy.pagination.PaginationHandler":{data:[2,3,1,""],data_all:[2,3,1,""],keys:[2,3,1,""],keys_all:[2,3,1,""],next:[2,3,1,""],return_bytes:[2,3,1,""],return_pretty:[2,3,1,""],to_dataframe:[2,3,1,""]},"zbpy.permissionentity":{PermConstraint:[2,2,1,""],PermEntry:[2,2,1,""],to_field_constraint:[2,1,1,""],to_field_constraints:[2,1,1,""]},"zbpy.permissionentity.PermEntry":{add_constraint:[2,3,1,""],to_protocol:[2,3,1,""]},"zbpy.util":{IdentityDefinition:[2,2,1,""],Nonce:[2,2,1,""],clean_string_for_filename:[2,1,1,""],empty_signature:[2,1,1,""],get_cert:[2,1,1,""],get_stub:[2,1,1,""],is_sem_ver_version_at_least:[2,1,1,""],new_account_interactive:[2,1,1,""],unwrap_zb_error:[2,1,1,""]},"zbpy.util.IdentityDefinition":{to_dict:[2,3,1,""]},"zbpy.util.Nonce":{get_nonce:[2,3,1,""]},"zbpy.zbprotocol_pb2_grpc":{ZetabaseProvider:[2,2,1,""],ZetabaseProviderServicer:[2,2,1,""],ZetabaseProviderStub:[2,2,1,""],add_ZetabaseProviderServicer_to_server:[2,1,1,""]},"zbpy.zbprotocol_pb2_grpc.ZetabaseProvider":{ConfirmNewIdentity:[2,5,1,""],CreateTable:[2,5,1,""],CreateUser:[2,5,1,""],DeleteObject:[2,5,1,""],GetData:[2,5,1,""],ListKeys:[2,5,1,""],ListSubIdentities:[2,5,1,""],ListTables:[2,5,1,""],LoginUser:[2,5,1,""],ModifySubIdentity:[2,5,1,""],PutData:[2,5,1,""],PutDataMulti:[2,5,1,""],QueryData:[2,5,1,""],RegisterNewIdentity:[2,5,1,""],SetPermission:[2,5,1,""],VersionInfo:[2,5,1,""]},"zbpy.zbprotocol_pb2_grpc.ZetabaseProviderServicer":{ConfirmNewIdentity:[2,3,1,""],CreateTable:[2,3,1,""],CreateUser:[2,3,1,""],DeleteObject:[2,3,1,""],GetData:[2,3,1,""],ListKeys:[2,3,1,""],ListSubIdentities:[2,3,1,""],ListTables:[2,3,1,""],LoginUser:[2,3,1,""],ModifySubIdentity:[2,3,1,""],PutData:[2,3,1,""],PutDataMulti:[2,3,1,""],QueryData:[2,3,1,""],RegisterNewIdentity:[2,3,1,""],SetPermission:[2,3,1,""],VersionInfo:[2,3,1,""]},zbpy:{auth:[2,0,0,"-"],basicqueries:[2,0,0,"-"],cleanqueries:[2,0,0,"-"],client:[2,0,0,"-"],cryptography:[2,0,0,"-"],datasci:[2,0,0,"-"],indexedfieldentity:[2,0,0,"-"],pagination:[2,0,0,"-"],permissionentity:[2,0,0,"-"],util:[2,0,0,"-"],zbcert:[2,0,0,"-"],zbprotocol_pb2:[2,0,0,"-"],zbprotocol_pb2_grpc:[2,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","function","Python function"],"2":["py","class","Python class"],"3":["py","method","Python method"],"4":["py","attribute","Python attribute"],"5":["py","staticmethod","Python static method"]},objtypes:{"0":"py:module","1":"py:function","2":"py:class","3":"py:method","4":"py:attribute","5":"py:staticmethod"},terms:{"boolean":2,"byte":2,"class":2,"default":2,"int":2,"new":2,"public":2,"return":2,"static":2,"true":2,Uses:2,Will:2,add:2,add_constraint:2,add_permiss:2,add_zetabaseproviderservicer_to_serv:2,addr:2,address:2,all:2,allow:2,allow_jwt:2,andexpress:2,ani:2,arrai:2,associ:2,attribut:2,audience_id:2,audience_typ:2,auth:1,auth_login_jwt:2,base:2,basicqueri:1,between:2,bool:2,byt:2,call_credenti:2,can:2,cell:2,certif:2,channel:2,channel_credenti:2,check:2,check_readi:2,check_vers:2,clean_string_for_filenam:2,cleanqueri:1,client:1,code:2,col_nam:2,col_typ:2,column:2,comment:2,comp_valu:2,compat:2,compress:2,confirm:2,confirm_new_sub_us:2,confirm_user_ident:2,confirmnewident:2,connect:2,constraint:2,content:[0,1],context:2,core:2,creat:2,create_t:2,createaccount:2,createt:2,createus:2,creation:2,credenti:2,credtyp:2,cryptographi:1,curv:2,data:2,data_al:2,data_typ:2,datafram:2,datapair:2,datasci:1,delet:2,delete_kei:2,delete_t:2,deleteobject:2,design:2,df_kei:2,df_to_kvp:2,dict:2,dictionari:2,document:2,done:2,dtype:2,ecdsa:2,ecdsa_credenti:2,ecdsasignatur:2,els:2,email:2,empti:2,empty_signatur:2,encod:2,encode_private_kei:2,encode_public_kei:2,entri:2,error:2,establish:2,except:2,exist:2,express:2,expression1:2,expression2:2,extra:2,extra_byt:2,fals:2,fastecdsa:2,field:2,field_nam:2,file:2,filenam:2,filepath:2,from:2,func:2,generate_key_pair:2,get:2,get_cert:2,get_credenti:2,get_nonc:2,get_stub:2,get_sub_ident:2,getdata:2,give:2,given:2,group_id:2,grpc_stub:2,handl:2,have:2,identitydefinit:2,ifs:2,import_kei:2,index:[0,2],index_typ:2,indexed_field:2,indexed_fields_to_protocol:2,indexedfield:2,indexedfieldent:1,insecur:2,insert:2,instanc:2,integ:2,interact:2,ipython:2,is_sem_ver_version_at_least:2,issu:2,item:2,iter:2,json:2,jwt:2,jwt_credenti:2,jwt_token:2,kei:2,keys_al:2,kwarg:2,lang_cod:2,languag:2,left:2,level:2,line:2,list:2,list_kei:2,list_tabl:2,listkei:2,listsubident:2,listtabl:2,listtablesrespons:2,locat:2,login:2,login_id:2,loginus:2,magic:2,make:2,make_credential_ecdsa:2,make_credential_jwt:2,make_zetabase_signatur:2,map:2,match:2,metadata:2,min_vers:2,miss:2,mobil:2,modifysubident:2,modul:[0,1],multi_put_extra_signing_byt:2,multipl:2,name:2,new_account_interact:2,new_sub_us:2,newaccount:2,next:2,nonc:2,none:2,numpi:2,object:2,one:2,option:2,orexpress:2,overwrit:2,own:2,p256:2,packag:[0,1],page:[0,2],pagin:1,paginationhandl:2,paginationrequest:2,pair:2,panda:2,paramet:2,paramt:2,parent_id:2,parse_df_column:2,parse_np_arrai:2,password:2,perm:2,permconstraint:2,permentri:2,permiss:2,permission_set_signing_byt:2,permission_signing_byt:2,permissionconstraint:2,permissionent:1,permissions_entry_signing_byt:2,permissionsentri:2,phone:2,piec:2,point:2,priv:2,priv_kei:2,priv_key_enc:2,privat:2,privatekei:2,privkei:2,proof:2,proofofcredenti:2,proto:2,pub:2,pub_kei:2,pub_key_enc:2,pubkei:2,publickei:2,put:2,put_data:2,put_datafram:2,put_dataframe_new_t:2,put_multi:2,put_np_arrai:2,putdata:2,putdatamulti:2,pwd:2,python:2,qry:2,queri:2,query_object_typifi:2,queryand:2,querydata:2,queryequ:2,querygreaterthan:2,querygreaterthanequ:2,querylessthan:2,querylessthanequ:2,querynotequ:2,queryor:2,queryord:2,querytextsearch:2,rais:2,readi:2,regist:2,registernewident:2,rel_byt:2,rel_data:2,rel_data_byt:2,req_valu:2,request:2,respect:2,return_byt:2,return_pretti:2,right:2,sdk:2,search:0,see:2,self:2,sent:2,server:2,servic:2,set:2,set_cert_verifi:2,set_id_kei:2,set_id_password:2,set_insecur:2,set_language_cod:2,set_par:2,set_server_addr:2,setpermiss:2,shell:2,sign_message_byt:2,signatur:2,signing_byt:2,signup_cod:2,special_data_byt:2,specifi:2,specify_field:2,standard_pagination_handl:2,start_entri:2,std_sigining_byt:2,std_signing_byt:2,string:2,stub:2,subident:2,subidentitieslist:2,submodul:1,subset:2,subus:2,subuser_id:2,tabl:2,table_create_signing_byt:2,table_id:2,table_owner_id:2,table_put_extra_signing_byt:2,tabledataformat:2,tableindexfield:2,tablesubqueri:2,target:2,thei:2,thi:2,through:2,timeout:2,to_datafram:2,to_dict:2,to_field_constraint:2,to_protocol:2,to_sub_queri:2,token:2,transform:2,tupl:2,type:2,uid:2,unwrap:2,unwrap_zb_error:2,user:2,user_id:2,user_vers:2,using:2,util:1,validate_signature_byt:2,valu:2,verif:2,verification_cod:2,verify_str:2,version:2,versiondetail:2,versioninfo:2,wait_for_readi:2,when:2,which:2,x_byte:2,you:2,your:2,zbcert:1,zberror:2,zbpprotocol_pb2:2,zbprotocol_pb2:1,zbprotocol_pb2_grpc:1,zetabas:2,zetabasecli:2,zetabaseclientstub:2,zetabaseprovid:2,zetabaseproviderservic:2,zetabaseproviderstub:2},titles:["Welcome to zbpy\u2019s documentation!","zbpy","zbpy package"],titleterms:{auth:2,basicqueri:2,cleanqueri:2,client:2,content:2,cryptographi:2,datasci:2,document:0,indexedfieldent:2,indic:0,modul:2,packag:2,pagin:2,permissionent:2,submodul:2,tabl:0,util:2,welcom:0,zbcert:2,zbprotocol_pb2:2,zbprotocol_pb2_grpc:2,zbpy:[0,1,2]}})
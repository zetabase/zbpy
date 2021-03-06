# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import zbprotocol_pb2 as zbprotocol__pb2


class ZetabaseProviderStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.VersionInfo = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/VersionInfo',
                request_serializer=zbprotocol__pb2.ZbEmpty.SerializeToString,
                response_deserializer=zbprotocol__pb2.VersionDetails.FromString,
                )
        self.ModifySubIdentity = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/ModifySubIdentity',
                request_serializer=zbprotocol__pb2.SubIdentityModify.SerializeToString,
                response_deserializer=zbprotocol__pb2.ZbError.FromString,
                )
        self.ListSubIdentities = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/ListSubIdentities',
                request_serializer=zbprotocol__pb2.SimpleRequest.SerializeToString,
                response_deserializer=zbprotocol__pb2.SubIdentitiesList.FromString,
                )
        self.RegisterNewIdentity = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/RegisterNewIdentity',
                request_serializer=zbprotocol__pb2.NewIdentityRequest.SerializeToString,
                response_deserializer=zbprotocol__pb2.NewIdentityResponse.FromString,
                )
        self.ConfirmNewIdentity = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/ConfirmNewIdentity',
                request_serializer=zbprotocol__pb2.NewIdentityConfirm.SerializeToString,
                response_deserializer=zbprotocol__pb2.ZbError.FromString,
                )
        self.PutData = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/PutData',
                request_serializer=zbprotocol__pb2.TablePut.SerializeToString,
                response_deserializer=zbprotocol__pb2.ZbError.FromString,
                )
        self.PutDataMulti = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/PutDataMulti',
                request_serializer=zbprotocol__pb2.TablePutMulti.SerializeToString,
                response_deserializer=zbprotocol__pb2.ZbError.FromString,
                )
        self.CreateTable = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/CreateTable',
                request_serializer=zbprotocol__pb2.TableCreate.SerializeToString,
                response_deserializer=zbprotocol__pb2.ZbError.FromString,
                )
        self.GetData = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/GetData',
                request_serializer=zbprotocol__pb2.TableGet.SerializeToString,
                response_deserializer=zbprotocol__pb2.TableGetResponse.FromString,
                )
        self.QueryData = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/QueryData',
                request_serializer=zbprotocol__pb2.TableQuery.SerializeToString,
                response_deserializer=zbprotocol__pb2.TableGetResponse.FromString,
                )
        self.QueryKeys = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/QueryKeys',
                request_serializer=zbprotocol__pb2.TableQuery.SerializeToString,
                response_deserializer=zbprotocol__pb2.ListKeysResponse.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/CreateUser',
                request_serializer=zbprotocol__pb2.NewSubIdentityRequest.SerializeToString,
                response_deserializer=zbprotocol__pb2.NewIdentityResponse.FromString,
                )
        self.SetPermission = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/SetPermission',
                request_serializer=zbprotocol__pb2.PermissionsEntry.SerializeToString,
                response_deserializer=zbprotocol__pb2.ZbError.FromString,
                )
        self.LoginUser = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/LoginUser',
                request_serializer=zbprotocol__pb2.AuthenticateUser.SerializeToString,
                response_deserializer=zbprotocol__pb2.AuthenticateUserResponse.FromString,
                )
        self.ListTables = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/ListTables',
                request_serializer=zbprotocol__pb2.ListTablesRequest.SerializeToString,
                response_deserializer=zbprotocol__pb2.ListTablesResponse.FromString,
                )
        self.ListKeys = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/ListKeys',
                request_serializer=zbprotocol__pb2.ListKeysRequest.SerializeToString,
                response_deserializer=zbprotocol__pb2.ListKeysResponse.FromString,
                )
        self.DeleteObject = channel.unary_unary(
                '/zbprotocol.ZetabaseProvider/DeleteObject',
                request_serializer=zbprotocol__pb2.DeleteSystemObjectRequest.SerializeToString,
                response_deserializer=zbprotocol__pb2.ZbError.FromString,
                )


class ZetabaseProviderServicer(object):
    """Missing associated documentation comment in .proto file"""

    def VersionInfo(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifySubIdentity(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSubIdentities(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterNewIdentity(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfirmNewIdentity(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PutData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PutDataMulti(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTable(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryKeys(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPermission(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoginUser(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTables(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListKeys(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteObject(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ZetabaseProviderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'VersionInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.VersionInfo,
                    request_deserializer=zbprotocol__pb2.ZbEmpty.FromString,
                    response_serializer=zbprotocol__pb2.VersionDetails.SerializeToString,
            ),
            'ModifySubIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.ModifySubIdentity,
                    request_deserializer=zbprotocol__pb2.SubIdentityModify.FromString,
                    response_serializer=zbprotocol__pb2.ZbError.SerializeToString,
            ),
            'ListSubIdentities': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSubIdentities,
                    request_deserializer=zbprotocol__pb2.SimpleRequest.FromString,
                    response_serializer=zbprotocol__pb2.SubIdentitiesList.SerializeToString,
            ),
            'RegisterNewIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterNewIdentity,
                    request_deserializer=zbprotocol__pb2.NewIdentityRequest.FromString,
                    response_serializer=zbprotocol__pb2.NewIdentityResponse.SerializeToString,
            ),
            'ConfirmNewIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfirmNewIdentity,
                    request_deserializer=zbprotocol__pb2.NewIdentityConfirm.FromString,
                    response_serializer=zbprotocol__pb2.ZbError.SerializeToString,
            ),
            'PutData': grpc.unary_unary_rpc_method_handler(
                    servicer.PutData,
                    request_deserializer=zbprotocol__pb2.TablePut.FromString,
                    response_serializer=zbprotocol__pb2.ZbError.SerializeToString,
            ),
            'PutDataMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.PutDataMulti,
                    request_deserializer=zbprotocol__pb2.TablePutMulti.FromString,
                    response_serializer=zbprotocol__pb2.ZbError.SerializeToString,
            ),
            'CreateTable': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTable,
                    request_deserializer=zbprotocol__pb2.TableCreate.FromString,
                    response_serializer=zbprotocol__pb2.ZbError.SerializeToString,
            ),
            'GetData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=zbprotocol__pb2.TableGet.FromString,
                    response_serializer=zbprotocol__pb2.TableGetResponse.SerializeToString,
            ),
            'QueryData': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryData,
                    request_deserializer=zbprotocol__pb2.TableQuery.FromString,
                    response_serializer=zbprotocol__pb2.TableGetResponse.SerializeToString,
            ),
            'QueryKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryKeys,
                    request_deserializer=zbprotocol__pb2.TableQuery.FromString,
                    response_serializer=zbprotocol__pb2.ListKeysResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=zbprotocol__pb2.NewSubIdentityRequest.FromString,
                    response_serializer=zbprotocol__pb2.NewIdentityResponse.SerializeToString,
            ),
            'SetPermission': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPermission,
                    request_deserializer=zbprotocol__pb2.PermissionsEntry.FromString,
                    response_serializer=zbprotocol__pb2.ZbError.SerializeToString,
            ),
            'LoginUser': grpc.unary_unary_rpc_method_handler(
                    servicer.LoginUser,
                    request_deserializer=zbprotocol__pb2.AuthenticateUser.FromString,
                    response_serializer=zbprotocol__pb2.AuthenticateUserResponse.SerializeToString,
            ),
            'ListTables': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTables,
                    request_deserializer=zbprotocol__pb2.ListTablesRequest.FromString,
                    response_serializer=zbprotocol__pb2.ListTablesResponse.SerializeToString,
            ),
            'ListKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.ListKeys,
                    request_deserializer=zbprotocol__pb2.ListKeysRequest.FromString,
                    response_serializer=zbprotocol__pb2.ListKeysResponse.SerializeToString,
            ),
            'DeleteObject': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteObject,
                    request_deserializer=zbprotocol__pb2.DeleteSystemObjectRequest.FromString,
                    response_serializer=zbprotocol__pb2.ZbError.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'zbprotocol.ZetabaseProvider', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ZetabaseProvider(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def VersionInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/VersionInfo',
            zbprotocol__pb2.ZbEmpty.SerializeToString,
            zbprotocol__pb2.VersionDetails.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifySubIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/ModifySubIdentity',
            zbprotocol__pb2.SubIdentityModify.SerializeToString,
            zbprotocol__pb2.ZbError.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSubIdentities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/ListSubIdentities',
            zbprotocol__pb2.SimpleRequest.SerializeToString,
            zbprotocol__pb2.SubIdentitiesList.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterNewIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/RegisterNewIdentity',
            zbprotocol__pb2.NewIdentityRequest.SerializeToString,
            zbprotocol__pb2.NewIdentityResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfirmNewIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/ConfirmNewIdentity',
            zbprotocol__pb2.NewIdentityConfirm.SerializeToString,
            zbprotocol__pb2.ZbError.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PutData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/PutData',
            zbprotocol__pb2.TablePut.SerializeToString,
            zbprotocol__pb2.ZbError.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PutDataMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/PutDataMulti',
            zbprotocol__pb2.TablePutMulti.SerializeToString,
            zbprotocol__pb2.ZbError.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/CreateTable',
            zbprotocol__pb2.TableCreate.SerializeToString,
            zbprotocol__pb2.ZbError.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/GetData',
            zbprotocol__pb2.TableGet.SerializeToString,
            zbprotocol__pb2.TableGetResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/QueryData',
            zbprotocol__pb2.TableQuery.SerializeToString,
            zbprotocol__pb2.TableGetResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryKeys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/QueryKeys',
            zbprotocol__pb2.TableQuery.SerializeToString,
            zbprotocol__pb2.ListKeysResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/CreateUser',
            zbprotocol__pb2.NewSubIdentityRequest.SerializeToString,
            zbprotocol__pb2.NewIdentityResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/SetPermission',
            zbprotocol__pb2.PermissionsEntry.SerializeToString,
            zbprotocol__pb2.ZbError.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoginUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/LoginUser',
            zbprotocol__pb2.AuthenticateUser.SerializeToString,
            zbprotocol__pb2.AuthenticateUserResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListTables(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/ListTables',
            zbprotocol__pb2.ListTablesRequest.SerializeToString,
            zbprotocol__pb2.ListTablesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListKeys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/ListKeys',
            zbprotocol__pb2.ListKeysRequest.SerializeToString,
            zbprotocol__pb2.ListKeysResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/zbprotocol.ZetabaseProvider/DeleteObject',
            zbprotocol__pb2.DeleteSystemObjectRequest.SerializeToString,
            zbprotocol__pb2.ZbError.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    # (http->django views is aded by default)
})
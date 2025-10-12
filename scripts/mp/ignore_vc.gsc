/#
# Make sure to have GameInterface enabled if you are going to use this
#/

init() {
    waittillframeend;
    thread moduleSetup();
}

moduleSetup() {
    level waittill( level.notifyTypes.gameFunctionsInitialized );
    scripts\_integration_shared::RegisterScriptCommand("PlayCommand",     "play",     "ply",  "play / add (to queue) a song", "User", "T6", false, ::null );
    scripts\_integration_shared::RegisterScriptCommand("StopCommand",     "stop",     "stp",  "stop the current song",        "User", "T6", false, ::null );
    scripts\_integration_shared::RegisterScriptCommand("NextCommand",     "next",     "nxt",  "play the next song in queue",  "User", "T6", false, ::null );
    scripts\_integration_shared::RegisterScriptCommand("PreviousCommand", "previous", "prev", "play / add (to queue) a song", "User", "T6", false, ::null );
}

null() { return; }
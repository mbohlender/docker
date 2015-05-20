function printKDEenv {
    echo "KDEHOME: $KDEHOME"
    echo "KDEDIR: $KDEDIR"
    echo "KDEDIRS: $KDEDIRS"
    echo "BUILD_DIR: $BUILD_DIR"
    echo "PATH: $PATH"
    echo "LD_LIBRARY_PATH: $LD_LIBRARY_PATH"
    echo "PKG_CONFIG_PATH: $PKG_CONFIG_PATH"
    echo "QT_PLUGIN_PATH: $QT_PLUGIN_PATH"
}

function akonadidb {
    mysql --auto-vertical-output -S $XDG_DATA_HOME/akonadi/socket-t420s.chrigi/mysql.socket akonadi
}

export KDEDIR=/opt/kde
export KDEHOME=$HOME/.kde4src/
export KDETMP=/tmp/$USER-kde4src
mkdir -p $KDETMP
export KDESYCOCA=/var/tmp/kdesycoca-custom

export KDEDIRS=$KDEDIR
export PATH=$KDEDIR/bin:$PATH
export LD_LIBRARY_PATH=$KDEDIR/lib:$KDEDIR/lib64
export PKG_CONFIG_PATH=$KDEDIR/lib/pkgconfig
export QT_PLUGIN_PATH=$KDEDIR/lib/kde4/plugins:$KDEDIR/lib64/kde4/plugins
export KDE4_AUTH_POLICY_FILES_INSTALL_DIR=$KDEDIR/usr/share/polkit-1/actions

# XDG
export XDG_CONFIG_HOME=$KDEHOME/.config
export XDG_DATA_HOME=$KDEHOME/.local/share
export XDG_CONFIG_DIRS=$KDEDIR/share/config
export XDG_DATA_DIRS=$KDEDIR/share/:/usr/share

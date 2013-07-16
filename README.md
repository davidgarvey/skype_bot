skype_bot
=========

Need a network socket to push nagios alerts into skype

Testing: echo "testing123" | nc localhost 50000



commands:

#SKYPE NOTIFICATIONS
#service
define command{
    command_name    notify-skype
    command_line    /usr/bin/printf "$NOTIFICATIONTYPE$ - $HOSTALIAS$/$SERVICEDESC$ is $SERVICESTATE$: $SERVICEOUTPUT$ ($$(hostname -s))" | nc -w 1 skypehost.name 50000
    }

#host
define command{
    command_name    host-notify-skype
    command_line    /usr/bin/printf "$NOTIFICATIONTYPE$ - $HOSTALIAS$ is $HOSTSTATE$: $HOSTOUTPUT$ ($$(hostname -s))" | nc -w 1 skypehost.name 50000
    }

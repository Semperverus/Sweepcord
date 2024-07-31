## Privacy-Friendly Alternatives to Discord
For those of you who would prefer to migrate away from Discord, there are a few options for you.

**NOTE:** when using the term 'server' below, this means an actual box that you or someone else is hosting the software on, _not_ a Discord lobby (Discord calls them "guilds" internally). When speaking about a Discord lobby, the word "server" will appear in air-quotes.

### 1. Matrix
[Matrix](https://matrix.org/) is not the most privacy-friendly entry on this list, but it is the closest in function and behavior to Discord. It supports "servers", private chats, and so on.

#### Privacy Pros and Cons
**PRO:** Matrix [provides their source-code](https://github.com/matrix-org). 
**PRO:** Matrix provides End-to-End encryption.  
**PRO:** Matrix does not require real identifiable information to sign up.  
**PRO:** Matrix can be self-hosted and federates (can talk to other servers like email).  
**CON:** Copies of (encrypted) messages and (unencrypted) metadata are cached on every server you interact with, not just your account's host.  
**CON:** Hosting your own server relies on Matrix's `vector.im` server for identity federation. Self-hosting this component has historically been very difficult.

### 2. Signal
[Signal](https://signal.org/) is by far the most privacy-respecting option on this list. However, it is more phone-focused than discord. It does support voice and video chat and group chats, but doesn't have "servers" (guilds) in the same way that Discord does.

**PRO:** Signal [provides their source-code](https://github.com/signalapp).  
**PRO:** Signal has been battle-tested in the US court on several occasions, and has proven via subpoena that [they keep almost no records](https://signal.org/bigbrother/central-california-grand-jury/).  
They keep:  
* Phone number used to sign up.  
* Time the account was created.  
* Time the account last accessed the service.

**PRO:** Signal encrypts literally everything. This includes the phone number you used to sign up with, your friends list, even sticker packs.  
**CON:** Signal requires you to sign up using a phone number.  
**CON:** Signal's desktop application is tethered to your phone via an encrypted communication channel as part of its security.  
**CON:** One of Signal's killer features as a phone-focused app, SMS support, was removed for security purposes.

### 3. XMPP
[XMPP](https://xmpp.org/) is more of a do-it-yourself solution for us nerdy folk. It falls somewhere inbetween Signal and Matrix in terms of privacy-friendliness, though this is largely up to how the server operator configures their server (i.e. the X in eXtensible Messaging and Presence Protocol).

**PRO:** Very self-hostable with software such as Prosody or EjabberD.  
**PRO:** Very flexible to your needs. The server softwares support a vibrant plugin system that implement many of XMPP's [XEPs](https://data.xmpp.net/explore/xmpp/xeps) (basically definitions of how new data can be sent).  
**PRO:** Can have full end-to-end encryption with Signal's Axolotl (a.k.a. OMEMO) encryption.  
**CON:** 
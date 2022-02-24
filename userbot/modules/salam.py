from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamualaikum Apakah Ada Give Away?**")


@register(outgoing=True, pattern='^.astg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Astagfirullah.... Gajelas amat**!!!!")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Waalaikumsalam Mari Mencari Give Away Bersamaku**")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇......")


@register(outgoing=True, pattern='^K(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Kesini Lah Teman Pejuang Rupiah**")


@register(outgoing=True, pattern='^N(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ni Pertanyaan Gajelas Amat**")


@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Berbagi Lah Sedikit Rejeki Mu!!!!**")


@register(outgoing=True, pattern='^M(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Mak Saya Menang Give Away!!**")


@register(outgoing=True, pattern='^Y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**YAUDAH DEH IYAA YANG NGASI PERTANYAAN SELALU BENAR**")


@register(outgoing=True, pattern='^C(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ciss Dulu Pejuang Give Away!!**")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Satu Dua Tigaa Saya Op Gada obat!!**")


@register(outgoing=True, pattern='^V(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**VERSI GA NIAT NGASI !!**")


@register(outgoing=True, pattern='^J(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JAUHKAN LAH HAMBA DARI ORANG GAJELAS YA ALLAH!!!**")


@register(outgoing=True, pattern='^A(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**AKU ADALAH RAJA MEKSIKO, EL MATADORE, SALVADOR, TEQUILA, DAN EL KONTOLE😆**")


@register(outgoing=True, pattern='^X(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DAHLAH SAYA TURUN GA PERNAH MENANG!!!**")


@register(outgoing=True, pattern='^Z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Zumbaaaaa Sayaaa Menaaaangg...**")


@register(outgoing=True, pattern='^H(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAHAHAHAHAHA INTINYA GIVE KALI INI UNTUK SAYA!**")


@register(outgoing=True, pattern='^O(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Oooooo Jadi Begituu, Paham Kok!!!**")


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Give Away Dulu Baru Kamu!!!**")

CMD_HELP.update({
    "salam":
    "P\
\nUsage: Untuk Memberi salam.\
\n\nL\
\nUsage: Untuk Menjawab Salam.\
\n\nK\
\nUsage: Untuk Mengajak Mereka.\
\n\nN\
\nUsage: Kalo kesel coba aja.\
\n\nB\
\nUsage: Buat Minta Give Away.\
\n\nM\
\nUsage: Tersedak Bahagia.\
\n\nY\
\nUsage: Buat yang males .\
\n\nC\
\nUsage: Ciss Pejuang.\
\n\nS\
\nUsage: Haha sokap."
})

CMD_HELP.update({
    "salam2":
    "V\
\nUsage: Orang caper.\
\n\nJ\
\nUsage: Minta Pertolongan.\
\n\nA\
\nUsage: Raja Meksiko.\
\n\nX\
\nUsage: Menyerah.\
\n\nZ\
\nUsage: Untuk Yang Menang.\
\n\nH\
\nUsage: Paling semangat.\
\n\n.astg\
\nUsage: Istighfar 1.\
\n\n.ast\
\nUsage: Istighfar 2.\
\n\nO\
\nUsage: Ngambek.\
\n\nG\
\nUsage: Liat Sendiri."
})

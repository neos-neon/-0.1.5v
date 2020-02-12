import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("네온봇준비완료")
    game = discord.Game("라마침뱃기")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("공지사항"):
        await message.channel.send("2월6일까지 탈것/갑옷거치대를 설치할시초기화될수있으니 그이후에 설치해주세요")
    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send("GOD국가에가입하신을축하드립니다앞으로국가에서즐거운시간보내세여")
    if message.content.startswith("네온봇"):
        await message.channel.send("봇제작/실험단계입니다!완성되면24시간호스트및명령어정리,노래봇등활용가능")
    if message.content.startswith("/오류신고"):
        await message.channel.send("{러버네온}네온네온#7112 디엠으로 신고해주세요!")
    if message.content.startswith("퇘"):
        await message.channel.send("칵퇘")
    if message.content.startswith("/경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트" )
        await author.add_roles(role)
    if message.content.startswith("/경고풀기"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)
    if message.content.startswith("/국민"):
        await message.channel.send("국가원등급부여완료!")
    if message.content.startswith("/국민"):
        author = message.guild.get_member(int(message.content[6:24]))
        role = discord.utils.get(message.guild.roles, name="국민")
        await author.add_roles(role)
    if message.content.startswith("!play 방구 소리"):
        await message.channel.send("한번더하면 네온네온이랑사귀는거임")
    if message.content.startswith("!play 네온"):
        await message.channel.send("한번더하면 감자임")
    if message.content.startswith("!stop"):
        await message.channel.send("!play")
    if message.content.startswith("!s"):
        await message.channel.send("칵퇘!")
    if message.content.startswith("!규칙"):
        await message.channel.send("'''노래방규칙'''"
                                   + "                                                            -신청하신노래가7분이상일경우스킵됩니다"
                                   + "                                             -같은신청곡으로 10번이상연속으로도배하시면 처벌을받으실수있습니다"
                                   + " -주크박스채널에혼자있을시 위규칙중'신청하신노래가7분이상일경우스킵됩니다'이란규칙은적용이안됩니다"
                                   + "'''채팅규칙'''"
                                   + "                                                              -노래방에서는 명령어만 쳐주세요"
                                   + "                                                   -욕을할시 경고가부여되며 정도에따라 밴이되실수있습니다"
                                   + "'''그의외의 규칙들'''"
                                   + "                                                 -단기간밴은 어떠한 해명도 주어진밴날짜들을줄일수없습니다"
                                   + "                                                          스텝들은 꼭 대통령께 밴허락을받아야합니다"
                                   + "                                                      스텝지시불이행시 대통령에의해처벌을받으실수있습니다")
    if message.content.startswith("!play 축지법"):
        await message.channel.send("축지법~!")
    if message.content.startswith("아!"):
        await message.channel.send("저씨")
    if message.content.startswith("뭐죠!"):
        await message.channel.send("감잔데요!")
    if message.content.startswith("))"):
        await message.channel.send("((")
    if message.content.startswith(";;"):
        await message.channel.send("yee")


client.run("Njc0NTM5MjU0NDI4NDY3MjAw.Xj0Zow.8I3lBwbvlhW8yP1EG-5SGrUUfMg")
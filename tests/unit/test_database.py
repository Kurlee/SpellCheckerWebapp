from SpellCheckApp.models import User, Post


def test_users_in_db(session):
    # UID 1
    gooduser1 = User(username='withphone', two_fa='1234567891')
    # UID 2
    gooduser2 = User(username='withphone1', two_fa='9999999999')
    # UID 3
    gooduser_nophone1 = User(username='nophone', two_fa='')

    """ Commit users to the DB """

    session.add(gooduser1)
    session.add(gooduser2)
    session.add(gooduser_nophone1)
    session.commit()

    assert gooduser1.id == 1
    assert gooduser2.id == 2
    assert gooduser_nophone1.id == 3

    """ Commit Posts to the DB """


def test_posts_in_db(session):
    body_clean1 = "This text has no misspellings"
    body_clean2 = "This text has no misspellings and contains some symbols: "
    body_clean_duplicate = "This text has no misspellings "
    body_dirty1 = "This text has one word misspelled: isntall"
    body_dirty2 = "This text has one word misspelled: catsss"
    body_dirty_xss = "This text has basic xss: <script>alert(1)</script>"
    body_dirty_afl = "This text has an AFL test case:\
                =================== \
                AFL ting test cases \
                ========= \
                  (See READwelcomegeneral il.) \
                 \
                The arcs/, images/, multimedia/, and others/ sudirPcto contain small, \
                staniles that can be used to seed ars for a \
                vqriety oI common data formats. \
                 \
                There is proÑably noth to be said about,tes, pt that themized for size and stripped of any nonential fluf∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑f. Some directories \
                contain sse varioˇ fÄ Ëres of the unÜerlying format. \
                For example, there is a PNG file with and wihouwelcomeor profile.ˇ \
                Additionak˝test es \
                are always welcome. \
                en starting f   d Ò     fuzzing jåbs benefit from a\
                sma~l and concise dictionary.See ../dictioÜaries/README.dictionarieboutr more."
    post1_clean = Post(body=body_clean1, user_id=1)
    post2_clean = Post(body=body_clean2, user_id=2)
    post3_clean = Post(body=body_clean_duplicate, user_id=1)
    post1_dirty = Post(body=body_dirty1, user_id=2)
    post2_dirty = Post(body=body_dirty2, user_id=1)
    post3_dirty = Post(body=body_dirty_xss, user_id=3)
    post4_dirty = Post(body=body_dirty_afl, user_id=3)

    session.add(post1_clean)
    session.add(post2_clean)
    session.add(post3_clean)
    session.add(post1_dirty)
    session.add(post2_dirty)
    session.add(post3_dirty)
    session.add(post4_dirty)

    session.commit()

    assert post1_dirty.get_author() == 'withphone1'



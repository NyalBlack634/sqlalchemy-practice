from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import or_
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

# DB接続
engine = create_engine('sqlite:///search_index2.db')

Base = declarative_base()


class Headline(Base):
    """Headlineモデル
    見出しを管理するテーブル

    Args:
        Base (sqlalchemy.orm.decl_api.DeclarativeMeta): ORMのベース
    """
    __tablename__ = 'headlines'

    '''見出しID(主キー)'''
    id = Column(Integer)
    id.primary_key = True
    '''新聞社名'''
    company = Column(String)
    '''発刊年'''
    year = Column(String)
    '''発刊月'''
    month = Column(String)
    '''発刊日+ページ'''
    page = Column(String)
    '''見出し画像パス'''
    path = Column(String)
    '''見出し画像の幅'''
    width = Column(Integer)
    '''見出し画像の高さ'''
    height = Column(Integer)
    '''見出し画像から抽出したテキスト'''
    text = Column(String)


def search_keyword(keyword: str, n: int):
    """キーワード検索(キーワード１つの場合)

    Args:
        keyword (str): 検索キーワード
        n (int): 引き出す見出し数

    Returns:
        _type_: _description_
    """
    return session.query(Headline).filter(Headline.text.like(f'%{keyword}%')).limit(n).all()


def search_keywords(keywords: list, n: int):
    """複数キーワードの部分一致

    Args:
        keywords (list): 検索キーワード
        n (int): 引き出す見出し数

    Returns:
        _type_: _description_
    """

    filters = [Headline.text.like(f'%{keyword}%') for keyword in keywords]

    return session.query(Headline).filter(or_(*filters)).limit(n).all()


if __name__ == '__main__':
    # セッションの生成
    Session = sessionmaker(bind=engine)
    session = Session()

    # headlines = session.query(Headline).limit(100).all()
    headlines = search_keywords(['別府'], 10)

    for headline in headlines:
        print(f'{headline.path}')
        print(f'width: {headline.width}, height: {headline.height}')
        print(headline.text)
        print('==' * 20)

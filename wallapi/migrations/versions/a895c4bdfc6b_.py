"""empty message

Revision ID: a895c4bdfc6b
Revises: b19ea692de3d
Create Date: 2021-05-26 00:19:46.291305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a895c4bdfc6b'
down_revision = 'b19ea692de3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('post_url', sa.String(), nullable=True),
    sa.Column('subreddit', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('nsfw', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###

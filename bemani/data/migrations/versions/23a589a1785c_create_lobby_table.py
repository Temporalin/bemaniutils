"""Create lobby table.

Revision ID: 23a589a1785c
Revises: 56dd21b994fe
Create Date: 2017-12-04 22:19:12.612743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23a589a1785c'
down_revision = '56dd21b994fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lobby',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game', sa.String(length=32), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('time', sa.Integer(), nullable=False),
    sa.Column('data', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('game', 'version', 'userid', name='game_version_userid'),
    mysql_charset='utf8mb4'
    )
    op.create_index(op.f('ix_lobby_time'), 'lobby', ['time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_lobby_time'), table_name='lobby')
    op.drop_table('lobby')
    # ### end Alembic commands ###
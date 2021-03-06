"""followers

Revision ID: 932711b524ef
Revises: d1efc110f7d4
Create Date: 2021-12-27 10:08:20.608570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '932711b524ef'
down_revision = 'd1efc110f7d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###

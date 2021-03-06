"""Move is_active to user table

Revision ID: 61dd58bdc80f
Revises: 00f55e83685a
Create Date: 2022-06-05 16:36:17.548370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61dd58bdc80f'
down_revision = '00f55e83685a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'is_active')
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_active')
    op.add_column('profiles', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

"""Create TableReservation

Revision ID: d4e486d19361
Revises: 532fd3389500
Create Date: 2023-06-06 20:09:19.724784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4e486d19361'
down_revision = '532fd3389500'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tables',
    sa.Column('table_id', sa.Integer(), nullable=False),
    sa.Column('start_armor', sa.TIMESTAMP(), nullable=True),
    sa.Column('end_armor', sa.TIMESTAMP(), nullable=True),
    sa.Column('waiter', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['waiter'], ['waiters.waiter_id'], ),
    sa.PrimaryKeyConstraint('table_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tables')
    # ### end Alembic commands ###

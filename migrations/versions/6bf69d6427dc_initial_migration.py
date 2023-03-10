"""Initial migration

Revision ID: 6bf69d6427dc
Revises:
Create Date: 2021-10-13 15:59:53.946823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bf69d6427dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assessments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1000), nullable=True),
    sa.Column('module_code', sa.String(length=1000), nullable=True),
    sa.Column('deadline', sa.Date(), nullable=True),
    sa.Column('description', sa.String(length=10000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_property_title'), 'property', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_property_title'), table_name='property')
    op.drop_table('property')
    # ### end Alembic commands ###

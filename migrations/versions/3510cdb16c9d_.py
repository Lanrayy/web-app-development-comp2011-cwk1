"""empty message

Revision ID: 3510cdb16c9d
Revises: 6bf69d6427dc
Create Date: 2021-10-13 16:22:04.993406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3510cdb16c9d'
down_revision = '6bf69d6427dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assessments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=1000), nullable=True),
    sa.Column('module_code', sa.String(length=1000), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=10000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_assessments_title'), 'assessments', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_assessments_title'), table_name='assessments')
    op.drop_table('assessments')
    # ### end Alembic commands ###
